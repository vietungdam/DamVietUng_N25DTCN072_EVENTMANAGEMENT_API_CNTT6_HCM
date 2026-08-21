from fastapi import APRouter, Depends, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.schemas.user import UserCreate, UserResponse
from app.services import auth_service

router = APRouter(prefix="/auth", tags=["Authentication"])

@router.post("/register", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
def register(user_data: UserCreate, db: Session = Depends(get_db)):
    """
    API Đăng ký tài khoản mới.
    """
    return auth_service.register_user(db=db, user_data=user_data)

@router.post("/login")
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    """
    API Đăng nhập, nhận về JWT Access Token (hỗ trợ Swagger UI qua OAuth2PasswordRequestForm).
    Lưu ý: Ô username trong Swagger tương ứng với email của bạn.
    """
    access_token = auth_service.authenticate_user(db=db, email=form_data.username, password=form_data.password)
    return {
        "access_token": access_token,
        "token_type": "bearer"
    }