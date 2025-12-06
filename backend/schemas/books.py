from pydantic import BaseModel
from datetime import datetime
from typing import Optional  # Added

class BookBase(BaseModel):
    title: str
    author: Optional[str] = None  # Changed from str | None
    price: float
    stock: int

class BookCreate(BookBase):
    pass

class BookRead(BookBase):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True