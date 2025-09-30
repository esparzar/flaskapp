# Flask Blog Application

A full-featured blog application built with Flask, featuring user authentication, blog post management, and a clean Bootstrap interface.

## Features

- User Authentication (Register, Login, Logout)
- Blog Post Management (Create, Read, Update)
- Responsive Bootstrap Design
- User-specific Content Management
- Pagination for Blog Posts
- Flash Messages for User Feedback
- SQLAlchemy Database Integration

## Tech Stack

- **Framework:** Flask
- **Database:** SQLAlchemy with SQLite
- **Authentication:** Flask-Login
- **Forms:** Flask-WTF
- **Frontend:** Bootstrap 5
- **Database Migrations:** Flask-Migrate

## Installation

1. Clone the repository:
```bash
git clone https://github.com/esparzar/flaskapp.git
cd flaskapp
```

2. Create and activate virtual environment:
```bash
python -m venv flaskevn
source flaskevn/bin/activate  # On Windows: flaskevn\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Initialize the database:
```bash
flask db upgrade
```

5. Create a test user and posts (optional):
```bash
python create_test_user.py
python create_test_posts.py
```

6. Run the application:
```bash
flask run
```

The application will be available at `http://127.0.0.1:5000/`

## Project Structure

```
flaskapp/
├── app/
│   ├── models/
│   │   ├── user.py
│   │   └── blog.py
│   ├── routes/
│   │   ├── auth.py
│   │   ├── blog.py
│   │   └── main.py
│   ├── templates/
│   │   ├── auth/
│   │   ├── blog/
│   │   └── main/
│   └── __init__.py
├── migrations/
├── config.py
├── requirements.txt
└── run.py
```

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

Distributed under the MIT License. See `LICENSE` for more information.

## Contact

Emmanuel Amponsah - esparzar535@gmail.com

Project Link: [https://github.com/esparzar/flaskapp](https://github.com/esparzar/flaskapp)