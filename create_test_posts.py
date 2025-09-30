from app import create_app, db
from app.models.blog import Blog
from app.models.user import User
from datetime import datetime

app = create_app()

with app.app_context():
    # Get the existing test user
    user = User.query.filter_by(username='testuser').first()
    if not user:
        print("Error: Test user not found. Please run create_test_user.py first.")
        exit(1)

    # Delete existing test posts if any
    Blog.query.delete()
    db.session.commit()

    # Create some test blog posts
    posts = [
        {
            'title': 'Baba News Room',
            'content': 'This is my first blog post! I\'m excited to share my thoughts and experiences with you all.',
            'created_at': datetime(2025, 9, 30, 10, 0)
        },
        {
            'title': 'Learning Flask Development',
            'content': 'Flask is a lightweight WSGI web application framework. It\'s designed to be simple and easy to extend. Here\'s what I\'ve learned so far...',
            'created_at': datetime(2025, 9, 30, 11, 0)
        },
        {
            'title': 'Python Tips and Tricks',
            'content': 'Python is an amazing language with many useful features. Today, I want to share some of my favorite Python tips and tricks that make coding easier.',
            'created_at': datetime(2025, 9, 30, 12, 0)
        }
    ]

    # Add the posts to the database
    for post_data in posts:
        post = Blog(
            title=post_data['title'],
            content=post_data['content'],
            author=user,
            created_at=post_data['created_at']
        )
        db.session.add(post)
    
    db.session.commit()
    print("Test posts have been created successfully!")