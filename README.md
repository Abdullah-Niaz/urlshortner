# URL Shortener

A lightweight Django-based URL shortening service that converts long URLs into clean, fast, and shareable short links. The application requires no authentication, provides a simple one-field input interface, and handles redirection seamlessly using unique slug generation.

---

## Features

* Generate unique URL slugs.
* Clean, modern UI with Tailwind, animations, and dark/light mode.
* Instant redirection to original URLs.
* Copy-to-clipboard functionality for short URLs.
* No authentication or user accounts required.
* Minimal, maintainable Django codebase.

---

## Tech Stack

* Python
* Django
* Tailwind CSS
* HTML templates
* SQLite (default) or any Django-supported database

---

## Project Structure

```
urlshortner/
│
├── manage.py
├── urlshortner/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
└── shortner/
    ├── migrations/
    ├── templates/
    │   └── shortener/
    │       └── home.html
    ├── static/ (optional)
    ├── models.py
    ├── utils.py
    ├── forms.py
    ├── views.py
    └── urls.py
```

---

## Installation

Clone the repository:

```
git clone https://github.com/yourusername/urlshortner.git
cd urlshortner
```

Create and activate a virtual environment:

```
python -m venv venv
venv\Scripts\activate  # Windows
source venv/bin/activate  # Linux/Mac
```

Install dependencies:

```
pip install -r requirements.txt
```

Run migrations:

```
python manage.py makemigrations
python manage.py migrate
```

Start the development server:

```
python manage.py runserver
```

Access the app at:

```
http://127.0.0.1:8000/
```

---

## How It Works

1. User enters a long URL into the input box.
2. A unique slug is generated with collision detection.
3. The slug is stored with the original URL.
4. Accessing `/abc123` redirects instantly to the original URL.

---

## Example

Input:

```
https://www.example.com/blog/article/1234567/very-long-url-here
```

Output:

```
http://127.0.0.1:8000/Xy9AbC
```

---

## Future Enhancements

* QR code generation for each short URL.
* Analytics dashboard with click counts.
* Custom slug support.
* API endpoint for programmatic shortening.
