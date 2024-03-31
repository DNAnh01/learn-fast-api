from datetime import datetime
from typing import Any, Dict, Generic, List, Optional, Type, TypeVar, Union

from fastapi import HTTPException, status
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel
from sqlalchemy import and_
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from app.common.string_case import decamelize
from app.common.utils import clone_model
from app.db.base_class import Base
from app.db.query_builder import get_count, get_filter, query_builder

ModelType = TypeVar("ModelType", bound=Base)
CreateSchemaType = TypeVar("CreateSchemaType", bound=BaseModel)
UpdateSchemaType = TypeVar("UpdateSchemaType", bound=BaseModel)


class CRUDBase(Generic[ModelType, CreateSchemaType, UpdateSchemaType]):
    def __init__(self, model: Type[ModelType]):
        """
        CRUD object with default methods to Create, Read, Update, Delete (CRUD).
        **Parameters**
        * `model`: A SQLAlchemy model class
        * `schema`: A Pydantic model (schema) class
        """
        self.model = model

    def get(self, db: Session, id: Any) -> Optional[ModelType]:
        return (
            db.query(self.model)
            .filter(self.model.id == id, self.model.deleted_at == None)
            .first()
        )

    def get_multi(
        self,
        db: Session,
        filter_param: dict = None,
    ) -> List[ModelType]:
        query = query_builder(
            db=db,
            model=self.model,
            filter=filter_param["filter"],
            order_by=filter_param["order_by"],
            include=filter_param["include"],
            join=filter_param["join"],
        )
        query = query.filter(self.model.deleted_at == None)
        return {
            "total": get_count(query),
            "results": query.offset(filter_param["skip"])
            .limit(filter_param["limit"])
            .all(),
        }

    def get_multi_not_paging(
        self,
        db: Session,
    ) -> List[ModelType]:
        query = query_builder(db=db, model=self.model)
        query = query.filter(self.model.deleted_at == None)
        return {
            "total": get_count(query),
            "results": query.all(),
        }

    def create(self, db: Session, *, obj_in: CreateSchemaType) -> ModelType:
        obj_in_data = decamelize(jsonable_encoder(obj_in))
        db_obj = self.model(**obj_in_data)  # type: ignore
        try:
            db.add(db_obj)
            db.commit()
            db.refresh(db_obj)
            return db_obj
        except IntegrityError as e:
            db.rollback()
            raise HTTPException(
                422, e.orig.diag.message_detail or "Key already exists"
            ) from None

    def update(
        self,
        db: Session,
        *,
        db_obj: ModelType,
        obj_in: Union[UpdateSchemaType, Dict[str, Any]],
    ) -> ModelType:
        obj_data = jsonable_encoder(db_obj)
        if isinstance(obj_in, dict):
            update_data = obj_in
        else:
            update_data = obj_in.dict(exclude_defaults=True)
        update_data = decamelize(update_data)
        for field in obj_data:
            if field in update_data:
                setattr(db_obj, field, update_data[field])
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def patch(
        self,
        db: Session,
        *,
        db_obj: ModelType,
        obj_in: Union[UpdateSchemaType, Dict[str, Any]],
    ) -> ModelType:
        obj_data = jsonable_encoder(db_obj)
        if isinstance(obj_in, dict):
            update_data = obj_in
        else:
            update_data = obj_in.dict(exclude_unset=True)
        update_data = decamelize(update_data)
        for field in obj_data:
            if field in update_data:
                setattr(db_obj, field, update_data[field])
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def remove(self, db: Session, *, id: int) -> ModelType:
        obj = db.query(self.model).get(id)
        obj.deleted_at = datetime.now()
        db.add(obj)
        db.commit()
        return obj

    def delete(self, db: Session, *, id: int):
        obj = db.query(self.model).get(id)
        db.delete(obj)
        db.commit()
        return obj

    def delete_obj(self, db: Session, *, obj):
        db.delete(obj)
        db.commit()
        return obj

    def get_one_or_fail(self, db: Session, id: Any) -> Optional[ModelType]:
        model = (
            db.query(self.model)
            .filter(self.model.id == id, self.model.deleted_at == None)
            .first()
        )
        if not model:
            self._throw_not_found_exception()
        return model

    def get_one_by_or_fail(self, db: Session, filter: dict = {}) -> Optional[ModelType]:
        model = self.get_one_by(db, filter)
        if not model:
            self._throw_not_found_exception()
        return model

    def get_one_by(self, db: Session, filter: dict = {}) -> Optional[ModelType]:
        return (
            db.query(self.model)
            .filter(and_(self.model.deleted_at == None, get_filter(self.model, filter)))
            .first()
        )

    def update_one_by(
        self,
        db: Session,
        filter: dict = {},
        obj_in: Union[UpdateSchemaType, Dict[str, Any]] = "{}",
    ) -> Optional[ModelType]:
        model = (
            db.query(self.model)
            .filter(and_(self.model.deleted_at == None, get_filter(self.model, filter)))
            .first()
        )

        if not model:
            return None

        return self.update(db=db, db_obj=model, obj_in=obj_in)

    def _throw_not_found_exception(self):
        raise HTTPException(
            status.HTTP_404_NOT_FOUND, detail=f"{self.model.__name__} not found"
        )

    def clone(self, db: Session, model: ModelType, modify: dict = {}):
        dict_ = {**clone_model(model), **modify}
        clone = self.model(**dict_)
        try:
            db.add(clone)
            db.commit()
            db.refresh(clone)
            return clone
        except IntegrityError as e:
            db.rollback()
            raise HTTPException(
                422, e.orig.diag.message_detail or "Key already exists"
            ) from None

    def save(self, db: Session, model: ModelType):
        db.add(model)
        db.commit()
        db.refresh(model)
        return model
