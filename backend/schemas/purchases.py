from pydantic import BaseModel
from datetime import datetime

class PurchaseBase(BaseModel):  # Fixed from BorrowBase
    user_id: int
    book_id: int

class PurchaseCreate(PurchaseBase):
    pass

class PurchaseRead(PurchaseBase):  # Changed from BorrowOut
    id: int
    date: datetime

    class Config:
        from_attributes = True  # Changed from orm_mode