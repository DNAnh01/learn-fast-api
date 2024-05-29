import json
from typing import Type, TypeVar

import sqlalchemy
from sqlalchemy import and_, func, or_
from sqlalchemy.orm import Session, selectinload
from sqlalchemy.sql.expression import cast

from app.db.base_class import Base

ModelType = TypeVar("ModelType", bound=Base)

# A
# filter={"title__like":"%a%"}
# --->>>   SELECT * FROM items WHERE title like '%a%'

# A and B
# filter={"title__ilike":"%a%", "id__gte":1}
# --->>>   SELECT * FROM items WHERE (title ilike '%a%') AND (id >= 1)

# A and B and C
# filter={"title__like":"%a%", "id__lt":10, "owner_id": 1}
# --->>>   SELECT * FROM items WHERE (title like '%a%') AND (id < 10) AND (owner_id = 1)

# A or B
# filter=[{"title__ilike":"%a%"}, {"id__gte":1}]
# --->>>   SELECT * FROM items WHERE (title ilike '%a%') OR (id >= 1)

# A or B or C
# filter=[{"title__like":"%a%"}, {"id__lt":10}, {"owner_id": 1}]
# --->>>   SELECT * FROM items WHERE (title like '%a%') OR (id < 10) OR (owner_id = 1)

# (A and B) or C
# filter=[{"title__like":"%a%", "id__lt":10}, {"owner_id": 1}]
# --->>>   SELECT * FROM items WHERE (title like '%a%' AND id < 10) OR owner_id = 1

# (A and B and C) or D
# filter=[{"title__like":"%a%", "id__lt":10, "id__gt": 1}, {"owner_id": 1}]
# --->>>   SELECT * FROM items WHERE (title like '%a%' AND id < 10 AND id > 1) OR owner_id = 1

# (A and B) or (C and D)
# filter=[{"title__like":"%a%", "id__lt":10}, {"id__gt": 1, "owner_id": 1}]
# --->>>   SELECT * FROM items WHERE (title like '%a%' AND id < 10) OR (id > 1 AND owner_id = 1)

# (A or B) and C
# filter={"0":[{"title__like":"%a%"}, {"owner_id": 1}], "owner_id__lte": 20}
# --->>>   SELECT * FROM items WHERE (title like '%a%' OR owner_id = 1) AND owner_id <= 20

# (A or B) and (C or D)
# filter={"0":[{"title__like":"%a%"}, {"owner_id": 1}], "1":[{"owner_id__lte": 20}, {"owner_id__gte": 10}]}
# --->>>   SELECT * FROM items WHERE (title like '%a%' OR owner_id = 1) AND (owner_id <= 20 OR owner_id >= 10)

# (A join B), filter B.id
# filter={"b.id__": "1"}
# join={'b': {}}
# --->>>   SELECT * FROM A a JOIN B b WHERE b.id = 1


def query_builder(
    db: Session,
    model: Type[ModelType],
    filter: str = None,
    order_by: str = None,
    include: str = None,
    join: str = None,
):
    query = db.query(model)

    if join is not None:
        for table in get_join_table(json.loads(join)):
            query = query.join(getattr(model, table))

    if filter is not None:
        filter = get_filter(model, json.loads(filter))
        query = query.filter(filter)

    if include is not None:
        include = get_include(include)
        query = query.options(*include)

    if order_by is not None:
        order_by = get_order_by(model, order_by)
        query = query.order_by(*order_by)
    return query


def get_class_by_tablename(tablename):
    """Return class reference mapped to table.

    :param tablename: String with name of table.
    :return: Class reference or None.
    """
    for c in Base._decl_class_registry.values():
        if hasattr(c, "__tablename__") and c.__tablename__ == tablename:
            return c


def get_join_table(join):
    if isinstance(join, dict):
        return [key for key, value in join.items()]
    return []


def get_filter(model: Type[ModelType], filters):
    if isinstance(filters, list):
        return or_(*[get_filter(model, filter) for filter in filters])

    if isinstance(filters, dict):
        sub_filters = [value for key, value in filters.items() if key.isnumeric()]
        ops_1 = [get_filter(model, sub_filter) for sub_filter in sub_filters]

        conditions = [cdt for cdt in filters.items() if not cdt[0].isnumeric()]
        ops_2 = [get_op(model, *cdt) for cdt in conditions]

        return and_(*ops_1, *ops_2)


def get_count(query):
    # counter = query.statement.with_only_columns([func.count()])
    # counter = counter.order_by(None)
    return query.with_entities(func.count()).scalar()


def get_include(include):
    return [selectinload(rlt) for rlt in include.split(",")]


def get_order_by(model, order_by):
    return [get_attr_order(model, attr) for attr in order_by.split(",")]


def get_attr_order(model, attr):
    if attr.startswith("-"):
        return getattr(model, attr[1:]).desc()
    return getattr(model, attr).asc()


def get_op(model: Type[ModelType], key: str, value: str):
    column = key.split("__")[0]

    if "." in key:
        column = column.split(".")[1]
        sub_key = key.split(".")[0]
        ref_instance = getattr(model, sub_key)
        instance_table_name = ref_instance.property.entity.mapped_table.name
        model = get_class_by_tablename(instance_table_name)

    op = getattr(model, column) == value
    if key.endswith("__lt"):
        op = getattr(model, column) < value
    if key.endswith("__lte"):
        op = getattr(model, column) <= value
    if key.endswith("__gte"):
        op = getattr(model, column) >= value
    if key.endswith("__gt"):
        op = getattr(model, column) > value
    if key.endswith("__neq"):
        op = getattr(model, column) != value
    if key.endswith("__like"):
        op = cast(getattr(model, column), sqlalchemy.String).like(f"%{value}%")
    if key.endswith("__ilike"):
        op = cast(getattr(model, column), sqlalchemy.String).ilike(f"%{value}%")
    if key.endswith("__in"):
        op = getattr(model, column).in_(value)
    if key.endswith("__nin"):
        op = ~getattr(model, column).in_(value)
    if key.endswith("__is"):
        op = getattr(model, column).is_(value)
    if key.endswith("__isn"):
        op = getattr(model, column).isnot(value)
    if key.endswith("__between"):
        op = getattr(model, column).between(*value)
    if key.endswith("__isnull"):
        if value == True:
            op = getattr(model, column).is_(None)
        else:
            op = getattr(model, column).isnot(None)
    return op
