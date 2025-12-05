from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from api.users import router as users_router
from api.books import router as books_router
from api.purchases import router as purchases_router
from api.borrows import router as borrows_router

from db.database import Base, engine


# ------------------------------------------------------
# Initialize app
# ------------------------------------------------------
app = FastAPI(
    title="Library API Backend",
    version="1.0.0",
    description="A full FastAPI backend for a library/bookhub system."
)

# ------------------------------------------------------
# Create database tables (if Alembic not used)
# ------------------------------------------------------
# Comment out if using Alembic migrations only


# ------------------------------------------------------
# CORS (allow frontend to connect)
# ------------------------------------------------------
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",   # React (Vite)
        "http://127.0.0.1:5173",
        "*"  # optional in development
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# ------------------------------------------------------
# Include Routers
# ------------------------------------------------------
app.include_router(users_router, prefix="/api", tags=["Users"])
app.include_router(books_router, prefix="/api", tags=["Books"])
app.include_router(purchases_router, prefix="/api", tags=["Purchases"])
app.include_router(borrows_router, prefix="/api", tags=["Borrows"])


# ------------------------------------------------------
# Root route
# ------------------------------------------------------
@app.get("/")
def root():
    return {
        "message": "Library API is running 🚀",
        "docs": "/docs",
        "redoc": "/redoc"
    }
