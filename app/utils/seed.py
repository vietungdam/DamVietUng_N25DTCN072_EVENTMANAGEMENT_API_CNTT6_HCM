from app.db.database import SessionLocal
from app.models.user import User
# Có thể dùng passlib để hash mật khẩu mẫu
import hashlib

def run_seed():
    db = SessionLocal()
    try:
        # Kiểm tra xem đã có user admin chưa
        admin = db.query(User).filter(User.email == "admin@example.com").first()
        if not admin:
            admin_user = User(
                email="admin@example.com",
                password_hash="dummy_hashed_password", # Thay bằng passlib hash thực tế ở phần Auth
                full_name="System Administrator",
                role="ADMIN",
                is_active=True
            )
            db.add(admin_user)
            db.commit()
            print("Đã seed tài khoản Admin thành công!")
        else:
            print("Dữ liệu seed đã tồn tại.")
    finally:
        db.close()

if __name__ == "__main__":
    run_seed()