# Quora Clone - Django Project

A simple Q&A web application inspired by Quora built using Django.  
Users can register, post and answer questions, like answers, and log out.

---

## 🔧 Tech Stack

- Python 3.12.0
- Django 5.2 
- Bootstrap 5 (for styling)  
- SQLite (default Django database)

---

## 🚀 Installation & Setup

Follow the steps below to get the project up and running on your local machine.

### 1. Clone the Repository

```bash
git clone https://github.com/abhishek173/Quora-Clone.git
cd Quora-Clone
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
source venv/bin/activate        # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

> If `requirements.txt` is not present, create it using:

```bash
pip freeze > requirements.txt
```

### 4. Apply Migrations

```bash
python manage.py migrate
```

### 5. Create a Superuser (Optional)

```bash
python manage.py createsuperuser
```

### 6. Run the Development Server

```bash
python manage.py runserver
```

Open your browser and go to:  
👉 [http://127.0.0.1:8000](http://127.0.0.1:8000)

---

## 📌 Features

- 🔐 User Authentication (Register, Login, Logout)
- ❓ Ask Questions
- 💬 Answer Questions
- 👍 Like Answers
- 🧑 Clean User Dashboard
- 🧱 Basic Bootstrap Layout inspired by Quora

---

## 📂 Project Structure

```
Quora-Clone/
├── core/
│   ├── migrations/
│   ├── templates/
│   │   ├── base.html
│   │   ├── login.html
│   │   ├── register.html
│   │   ├── home.html
│   │   ├── post_question.html
│   │   └── question_detail.html
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── urls.py
│   └── views.py
├── db.sqlite3
├── manage.py
├── requirements.txt
└── README.md
```

---


## 💡 Author

Developed by [Abhishek Kumar](https://github.com/abhishek173) 💻
