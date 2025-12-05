from pydantic import BaseModel
from datetime import datetime

class BookBase(BaseModel):
    title: str
    author: str | None = None
    price: float
    stock: int

class BookCreate(BookBase):
    pass

class BookOut(BookBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True
