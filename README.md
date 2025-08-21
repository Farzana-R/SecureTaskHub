# 🔐 SecureTaskHub

A secure team and task management system built with **Django**.  
The project focuses on **security best practices** and **complex ORM queries**, making it a great showcase for learning and demonstrating Django skills.

---

## 🚀 Features
- Custom **User model** with roles: **Admin, Manager, Employee**
- Role-based access control
- Secure authentication (login, logout, password management)
- Task management system with role restrictions
- ORM-powered analytics and reporting (upcoming)
- Audit logging with signals (upcoming)

---

## 🛠 Tech Stack
- **Backend**: Django 4.x, Python 3.10+
- **Database**: SQLite (dev), PostgreSQL (recommended for production)
- **Frontend**: Django Templates + Bootstrap/Tailwind
- **Authentication**: Django Auth
- **Security**: CSRF, XSS protection, secure session/cookie settings

---

## 📦 Installation

```bash
# clone repo
git clone https://github.com/your-username/securetaskhub.git
cd securetaskhub

# create virtual env
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows

# install dependencies
pip install -r requirements.txt

# run migrations
python manage.py makemigrations
python manage.py migrate

# create superuser
python manage.py createsuperuser

# run dev server
python manage.py runserver

📜 License

MIT License