from flask import Blueprint

# Create blueprints
main_bp = Blueprint('main', __name__)
auth_bp = Blueprint('auth', __name__, url_prefix='/auth')
blog_bp = Blueprint('blog', __name__)

# Import routes after blueprint creation to avoid circular imports
from .main import *
from .auth import *
from .blog import *

# This allows us to import blueprints directly from the routes package
__all__ = ['main_bp', 'auth_bp', 'blog_bp']
