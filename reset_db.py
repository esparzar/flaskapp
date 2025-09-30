from app import create_app, db
from app.models.user import User

app = create_app()

with app.app_context():
    # Delete existing users
    User.query.delete()
    db.session.commit()
    
    # Create fresh test user
    user = User(username='testuser', email='test@example.com')
    user.set_password('password123')
    db.session.add(user)
    db.session.commit()
    print("Database reset and test user created successfully!")