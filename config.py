import os

class Config:
    # Security
    SECRET_KEY = 'your-secret-key-change-this'
    
    # Database
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    # File Upload
    UPLOAD_FOLDER = os.path.join('app', 'static', 'avatars')
    MAX_CONTENT_LENGTH = 1024 * 1024  # 1MB max file size
    ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
