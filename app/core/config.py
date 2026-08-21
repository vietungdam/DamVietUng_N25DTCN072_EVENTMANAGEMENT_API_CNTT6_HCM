# ==============================================================================
# FILE CẤU HÌNH TRUNG TÂM (Central Configuration)
# ==============================================================================

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    # --- Cấu hình ứng dụng ---
    APP_NAME: str = "Event Management API"
    APP_VERSION: str = "1.0.0"
    APP_DESCRIPTION: str = "Ứng dụng quản lý sự kiện với FastAPI."

    # --- Cấu hình Database ---
    DATABASE_URL: str

    # --- Cấu hình JWT ---
    SECRET_KEY: str
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60

    # --- Cấu hình CORS ---
    ALLOWED_ORIGINS: list[str] = ["http://localhost:3000", "http://localhost:5173"]

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


# Khởi tạo instance dùng chung cho toàn bộ ứng dụng
settings = Settings()