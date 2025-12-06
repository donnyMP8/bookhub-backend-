from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List  # Added
from db.database import get_db
from services.recommendations import get_user_recommendations
from schemas.books import BookRead

router = APIRouter(prefix="/recommendations", tags=["Recommendations"])


@router.get("/{user_id}", response_model=List[BookRead])  # Changed from list[BookRead]
def recommend(user_id: int, db: Session = Depends(get_db)):
    recs = get_user_recommendations(db, user_id)
    return recs