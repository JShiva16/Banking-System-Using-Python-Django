# 🏦 Banking Management System

A full-stack banking application built with Django that enables secure account management, transaction processing, fund transfers, and automated interest calculation through background task scheduling.

The system demonstrates practical implementation of web development, database management, authentication, and asynchronous task processing in a real-world banking environment.

---

## 🚀 Features

### 👤 User Account Management

* User registration and authentication
* Secure login and logout
* Profile management
* Account balance tracking

### 💰 Banking Operations

* Deposit funds
* Withdraw funds with balance validation
* Transfer funds between accounts
* Real-time balance updates

### 📊 Transaction Management

* Complete transaction history
* Transaction reporting
* Account activity tracking
* Detailed transaction records

### ⚙️ Automated Interest Calculation

* Background task processing using Celery
* Scheduled interest accrual
* Automatic balance updates
* Redis-powered task queue

### 🔐 Security Features

* Django authentication system
* CSRF protection
* Password hashing
* Form validation
* ORM-based SQL injection prevention

---

## 🛠️ Tech Stack

### Backend

* Python
* Django

### Database

* SQLite (Development)
* PostgreSQL (Production Ready)

### Task Scheduling

* Celery
* Redis

### Frontend

* HTML5
* CSS3
* Bootstrap

### Deployment

* Gunicorn
* Vercel

---

## 📂 Project Structure

```text
banking-system/
│
├── accounts/
│   ├── models.py
│   ├── views.py
│   ├── forms.py
│   └── urls.py
│
├── transactions/
│   ├── models.py
│   ├── views.py
│   ├── tasks.py
│   └── urls.py
│
├── core/
│   ├── views.py
│   └── urls.py
│
├── banking_system/
│   ├── settings.py
│   ├── urls.py
│   ├── celery.py
│   └── wsgi.py
│
├── templates/
├── static/
├── manage.py
├── requirements.txt
└── db.sqlite3
```

---

## ⚡ Installation

### Clone Repository

```bash
git clone https://github.com/JShiva16/Banking-System-Using-Python-Django.git
cd Banking-System-Using-Python-Django/banking-system
```

### Create Virtual Environment

**Windows**

```bash
python -m venv venv
venv\Scripts\activate
```

**Linux / macOS**

```bash
python3 -m venv venv
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Apply Migrations

```bash
python manage.py migrate
```

### Create Admin User

```bash
python manage.py createsuperuser
```

### Start Development Server

```bash
python manage.py runserver
```

Open:

```text
http://127.0.0.1:8000/
```

---

## 🔄 Running Celery Background Tasks

### Start Celery Worker

```bash
celery -A banking_system worker -l info
```

### Start Celery Beat Scheduler

```bash
celery -A banking_system beat -l info
```

These services automatically calculate and credit interest to eligible accounts.

---

## 📋 Main Functionalities

| Module          | Description                    |
| --------------- | ------------------------------ |
| Registration    | Create new user accounts       |
| Authentication  | Secure login and logout        |
| Deposit         | Add funds to account           |
| Withdraw        | Withdraw available balance     |
| Transfer        | Transfer money between users   |
| Reports         | View transaction history       |
| Interest Engine | Automated interest calculation |
| Admin Panel     | Manage users and transactions  |

---

## 📌 Application Workflow

1. User creates an account
2. User logs into the system
3. User performs banking operations
4. Transactions are recorded in the database
5. Celery executes scheduled interest calculations
6. Updated balances are reflected in user accounts
7. Users can view complete transaction history

---

## 🔗 Application Routes

| Route            | Description         |
| ---------------- | ------------------- |
| `/`              | Home Page           |
| `/register/`     | User Registration   |
| `/login/`        | User Login          |
| `/logout/`       | User Logout         |
| `/deposit/`      | Deposit Funds       |
| `/withdraw/`     | Withdraw Funds      |
| `/transfer/`     | Transfer Funds      |
| `/transactions/` | Transaction History |
| `/admin/`        | Django Admin Panel  |

---

## 🔐 Security Measures

* Django Authentication Framework
* Secure Password Hashing
* Session Management
* CSRF Protection
* Form Validation
* Database ORM Protection
* Transaction Validation Checks



## 🎯 Learning Outcomes

This project demonstrates practical experience with:

* Full-Stack Web Development
* Django Framework
* Database Design & Management
* Authentication Systems
* Background Task Scheduling
* RESTful Architecture Concepts
* Financial Transaction Processing
* Deployment & Production Configuration


