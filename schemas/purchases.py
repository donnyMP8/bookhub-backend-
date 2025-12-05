from pydantic import BaseModel
from datetime import datetime

class PurchaseBase(BaseModel):
    user_id: int
    book_id: int

class PurchaseCreate(PurchaseBase):
    pass

class PurchaseOut(PurchaseBase):
    id: int
    date: datetime

    class Config:
        orm_mode = True
