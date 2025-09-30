from app import create_app, db
from app.models import User

app = create_app()

with app.app_context():
    # Create test user
    user = User(username='test_user', email='test@example.com')
    user.set_password('password123')
    db.session.add(user)
    db.session.commit()
    print("Test user created successfully!")
    print("Username: test_user")
    print("Password: password123")