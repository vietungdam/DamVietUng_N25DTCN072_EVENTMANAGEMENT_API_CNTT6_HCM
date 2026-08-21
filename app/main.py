from fastapi import FastAPI, Request, status, HTTPException
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from app.db.database import engine, Base
# Import models để SQLAlchemy nhận diện khi tạo bảng
from app.models import user, event, event_task

# Khởi tạo bảng trong database
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Event Management API", version="1.0.0")

# Exception handling cơ bản
@app.exception_handler(HTTPException)
async def http_exception_handler(request: Request, exc: HTTPException):
    return JSONResponse(
        status_code=exc.status_code,
        content={"detail": exc.detail},
    )

@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    return JSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        content={"detail": "Validation error", "message": exc.errors()},
    )

@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    return JSONResponse(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        content={"detail": "Internal server error", "message": str(exc)},
    )

@app.get("/health", tags=["Health Check"])
def health_check():
    return {"status": "ok", "message": "Database and server are running successfully"}