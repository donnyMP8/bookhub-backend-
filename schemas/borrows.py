from pydantic import BaseModel
from datetime import datetime

class BorrowBase(BaseModel):
    user_id: int
    book_id: int

class BorrowCreate(BorrowBase):
    pass

class BorrowOut(BorrowBase):
    id: int
    borrowed_at: datetime
    returned: bool

    class Config:
        orm_mode = True
