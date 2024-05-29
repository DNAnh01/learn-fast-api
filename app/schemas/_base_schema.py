from datetime import datetime
from typing import ClassVar, Optional

import pydantic


class BaseSchema(pydantic.BaseModel):
    IS_ACTIVE: ClassVar[str] = "is_active"
    CREATED_AT: ClassVar[str] = "created_at"
    UPDATED_AT: ClassVar[str] = "updated_at"
    DELETED_AT: ClassVar[str] = "deleted_at"

    is_active: Optional[bool] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    deleted_at: Optional[datetime] = None