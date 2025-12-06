from pydantic import BaseModel
from datetime import datetime

class BorrowBase(BaseModel):
    user_id: int
    book_id: int

class BorrowCreate(BorrowBase):
    pass

class BorrowRead(BorrowBase):  # Changed from BorrowOut
    id: int
    borrowed_at: datetime
    returned: bool

    class Config:
        from_attributes = True  # Changed from orm_mode