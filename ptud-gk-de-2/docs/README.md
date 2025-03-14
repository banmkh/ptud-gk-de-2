# Task Manager - PTUD GK Đề 2

## 📌 Thông tin cá nhân
- **Họ và tên:** Đoàn Vũ Thiên Ban
- **MSSV:** 22710261

## 📖 Mô tả dự án
Task Manager là một ứng dụng web giúp người dùng quản lý công việc cá nhân với các tính năng chính:
- Đăng ký, đăng nhập và phân quyền người dùng (`Admin` và `User`).
- Thêm, cập nhật trạng thái (`Pending`, `Completed`), và xóa công việc.
- Hiển thị danh sách công việc dưới dạng `Card-based`.
- Upload avatar cho người dùng.
- Giao diện tối ưu với `Bootstrap 5`.

## 🚀 Hướng dẫn cài đặt
### 1️⃣ **Clone Repository**
```bash
git clone https://github.com/YOUR_USERNAME/ptud-gk-de-2.git
cd ptud-gk-de-2
```

### 2️⃣ **Tạo môi trường ảo (khuyến khích)**
```bash
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate    # Windows
```

### 3️⃣ **Cài đặt các thư viện cần thiết**
```bash
pip install -r requirements.txt
```

### 4️⃣ **Khởi tạo Database**
```bash
python
```
```python
from app import db
with app.app_context():
    db.create_all()
exit()
```

### 5️⃣ **Chạy ứng dụng**
```bash
python app.py
```
Mở trình duyệt và truy cập: **`http://127.0.0.1:5000/`**

## 👤 Đăng nhập tài khoản mặc định
| Username | Password | Role  |
|----------|----------|-------|
| admin    | admin123 | Admin |
| user     | user123  | User  |

## 🛠 Công nghệ sử dụng
- **Flask** - Backend API
- **SQLite** - Database
- **Bootstrap 5** - Frontend UI
- **Werkzeug** - Hash mật khẩu

---
📌 *Liên hệ: [Email của bạn]*
