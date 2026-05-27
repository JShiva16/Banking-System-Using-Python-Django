
A comprehensive Django-based banking application with account management, transaction processing, and automated interest calculation using Celery scheduled tasks.

## 🎯 Features

- **User Account Management** - User registration, login, and profile management
- **Transaction Processing** - Deposit, withdrawal, and transfer functionality
- **Interest Calculation** - Automated interest accrual using Celery background tasks
- **Transaction Reports** - Detailed transaction history and reporting
- **Secure Authentication** - User authentication and session management
- **Responsive UI** - Clean and user-friendly interface

## 🛠️ Technologies Used

- **Backend Framework**: Django
- **Database**: SQLite (development), PostgreSQL (production-ready)
- **Task Queue**: Celery with Redis
- **Frontend**: HTML5, CSS3, Bootstrap
- **Server**: Gunicorn (production)
- **Deployment**: Vercel

## 📋 Prerequisites

Before you begin, ensure you have the following installed:

- Python 3.8 or higher
- pip (Python package installer)
- Redis (for Celery task queue)
- Git

## 🚀 Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/JShiva16/Banking-System-Using-Python-Django.git
cd Banking-System-Using-Python-Django/banking-system
```

### 2. Create and Activate Virtual Environment

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Apply Database Migrations

```bash
python manage.py migrate
```

### 5. Create a Superuser (Admin)

```bash
python manage.py createsuperuser
```

### 6. Run Development Server

```bash
python manage.py runserver
```

The application will be available at `http://127.0.0.1:8000/`

### 7. Run Celery (Optional - For Background Tasks)

In a separate terminal:

```bash
celery -A banking_system worker -l info
```

And in another terminal for Celery Beat (scheduler):

```bash
celery -A banking_system beat -l info
```

## 📁 Project Structure

```
banking-system/
├── accounts/                 # User authentication & profile management
│   ├── models.py            # User models
│   ├── views.py             # Login/registration views
│   ├── forms.py             # User forms
│   └── urls.py              # URL routing
├── transactions/            # Transaction handling
│   ├── models.py            # Transaction models
│   ├── views.py             # Transaction views
│   ├── tasks.py             # Celery tasks (interest calculation)
│   └── urls.py              # URL routing
├── core/                    # Core app (homepage, general views)
│   ├── views.py             # Core views
│   └── urls.py              # URL routing
├── banking_system/          # Project settings
│   ├── settings.py          # Django settings
│   ├── urls.py              # Main URL configuration
│   ├── wsgi.py              # WSGI configuration
│   └── celery.py            # Celery configuration
├── templates/               # HTML templates
├── static/                  # CSS, JavaScript, images
├── manage.py                # Django management script
├── requirements.txt         # Python dependencies
└── db.sqlite3              # SQLite database
```

## 🔑 Key Features Explained

### Account Management
- User registration with email verification
- Secure login/logout
- Password management
- Account balance tracking

### Transactions
- Deposit funds into account
- Withdraw funds (with balance validation)
- Transfer funds between accounts
- View transaction history and generate reports

### Background Tasks (Celery)
- Automated daily interest calculation
- Interest is credited to user accounts
- Scheduled tasks run at specified intervals

## ⚙️ Configuration

### Important: Before Deployment

1. Update `banking_system/settings.py`:
   - Set `DEBUG = False`
   - Generate a new `SECRET_KEY`
   - Update `ALLOWED_HOSTS` with your domain
   - Configure email settings for production
   - Set up proper database (PostgreSQL recommended)

2. Environment Variables:
   Create a `.env` file with:
   ```
   SECRET_KEY=your-secret-key
   DEBUG=False
   DATABASE_URL=your-database-url
   REDIS_URL=your-redis-url
   ```

### Database

**Development**: SQLite (included)
**Production**: PostgreSQL (recommended)

## 📊 Admin Panel

Access the Django admin panel at: `http://127.0.0.1:8000/admin/`

Login with your superuser credentials to manage users, transactions, and accounts.

## 🔐 Security Features

- CSRF protection enabled
- Secure password hashing
- User authentication required for transactions
- Input validation on all forms
- SQL injection prevention via ORM

## 📝 API Endpoints (Main Views)

- `/` - Home page
- `/register/` - User registration
- `/login/` - User login
- `/logout/` - User logout
- `/transactions/` - View transactions
- `/deposit/` - Deposit funds
- `/withdraw/` - Withdraw funds
- `/transfer/` - Transfer funds
- `/admin/` - Admin panel

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 📞 Contact

**Author**: JShiva16  
**GitHub**: [@JShiva16](https://github.com/JShiva16)  
**Project**: [Banking-System-Using-Python-Django](https://github.com/JShiva16/Banking-System-Using-Python-Django)

## 🐛 Troubleshooting

### Issue: ModuleNotFoundError
**Solution**: Make sure your virtual environment is activated and all dependencies are installed.

### Issue: Database errors
**Solution**: Run `python manage.py migrate` to apply all migrations.

### Issue: Static files not loading
**Solution**: Run `python manage.py collectstatic` in production.

### Issue: Celery tasks not running
**Solution**: Ensure Redis is running and Celery worker is started in a separate terminal.

## 📚 Additional Resources

- [Django Documentation](https://docs.djangoproject.com/)
- [Celery Documentation](https://docs.celeryproject.org/)
- [Django REST Framework](https://www.django-rest-framework.org/)

---

**Happy Banking! 🏦**
