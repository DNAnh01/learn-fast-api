from typing import Optional

from app.common.string_case import convert_filter_to_camel_case, to_snake_case


async def common_filter_parameters(
    page: int = 1,
    limit: int = 100,
    filter: str = "{}",
    include: str = None,
    join: str = "{}",
    orderBy: str = None,
):
    if join:
        join_ = convert_filter_to_camel_case(join)
    else:
        join_ = "{}"

    if filter:
        filter_ = convert_filter_to_camel_case(filter)
    else:
        filter_ = "{}"

    if include:
        include = to_snake_case(include)
    else:
        include = None
    skip = (page - 1) * limit
    if skip < 1:
        skip = 0
    if orderBy and orderBy != "":
        orderBy = to_snake_case(orderBy)
    else:
        orderBy = None
    return {
        "skip": skip,
        "limit": limit,
        "filter": filter_,
        "include": include,
        "order_by": orderBy,
        "join": join_,
    }


async def common_filter_parameters_chat_bot(
    page: int = 1,
    limit: int = 100,
    filter: str = "{}",
    include: str = None,
    orderBy: str = None,
    chatBotId: Optional[int] = None,
    join: str = "{}",
):
    if filter:
        filter_ = convert_filter_to_camel_case(filter)
    else:
        filter_ = "{}"
    if include:
        include = to_snake_case(include)
    else:
        include = None
    skip = (page - 1) * limit
    if skip < 1:
        skip = 0
    if join:
        join_ = convert_filter_to_camel_case(join)
    else:
        join_ = "{}"
    if orderBy and orderBy != "":
        orderBy = to_snake_case(orderBy)
    else:
        orderBy = None
    return {
        "skip": skip,
        "limit": limit,
        "filter": filter_,
        "include": include,
        "order_by": orderBy,
        "chat_bot_id": chatBotId,
        "join": join_,
    }


async def gitlab_pagination(page: int = 1, limit: int = 100, search: str = ""):
    return {"page": page, "size": limit, "search": search}


async def stripe_pagination(startingAfter=None, limit: int = 100):
    return {"starting_after": startingAfter, "limit": limit}
