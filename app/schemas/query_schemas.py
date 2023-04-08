from pydantic import BaseModel, Field

from .services.enums import Ordering


class PaginationQuerySchema(BaseModel):
    limit: int = Field(gt=0)
    offset: int = Field(ge=0)
    ordering: Ordering = Ordering.asc
