from pydantic import BaseModel, EmailStr
from datetime import datetime

class UserBase(BaseModel):
    name: str
    email: EmailStr

class UserCreate(UserBase):
    pass

class UserRead(UserBase):  # Changed from UserOut
    id: int
    created_at: datetime

    class Config:
        from_attributes = True  # Changed from orm_mode