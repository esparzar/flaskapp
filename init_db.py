from app import db, create_app

def init_db():
    app = create_app()
    with app.app_context():
        db.create_all()
        print("Database tables created successfully!")