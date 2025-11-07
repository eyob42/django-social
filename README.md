# django-social

A small Django social app (dwitter-like) that demonstrates user profiles and short "dweets" (posts).

This repository contains a Django project with a `dwitter` app and the project package `social`.

A Django-based social application template.  
Built with Django and HTML templates — a simple starting point for social media-style features.

## Features

- User authentication (signup, login, logout)
- User profiles
- Create, edit, and delete posts
- Commenting and liking system
- Responsive front-end templates

## Getting Started

### Prerequisites

- Python 3.x
- Django 4.x
- pip

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/eyob42/django-social.git
   cd django-social
   ```

2. Create and activate a virtual environment:

   ```bash
   python -m venv env
   env\Scripts\activate   # On Windows
   # source env/bin/activate   # On macOS/Linux
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

### Database Setup

Run migrations:

```bash
python manage.py makemigrations
python manage.py migrate
```

(Optional) Create a superuser:

```bash
python manage.py createsuperuser
```

### Run the Development Server

```bash
python manage.py runserver
```

Then open your browser and visit:

```
http://127.0.0.1:8000/
```

## Folder Structure

```
django-social/
│
├─ social/           # Main Django app
│   ├─ migrations/
│   ├─ static/
│   ├─ templates/
│   ├─ models.py
│   ├─ views.py
│   └─ urls.py
│
├─ manage.py
├─ requirements.txt
└─ README.md
```

## Contributing

1. Fork the repository
2. Create a new branch (`git checkout -b feature-name`)
3. Commit changes (`git commit -m "Add feature"`)
4. Push the branch (`git push origin feature-name`)
5. Open a Pull Request

## License

MIT License

## Author

**Eyob Adigeh**
GitHub: [eyob42](https://github.com/eyob42)
