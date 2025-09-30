from flask import Blueprint, render_template, jsonify
from app.models.blog import Blog

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def index():
    recent_posts = Blog.query.order_by(Blog.created_at.asc()).limit(5).all()
    print("Recent posts:", recent_posts)  # Debug print
    return render_template('index.html', recent_posts=recent_posts)

@main_bp.route('/health')
def health():
    return jsonify({'status': 'ok'})

@main_bp.route('/about')
def about():
    return render_template('main/about.html')