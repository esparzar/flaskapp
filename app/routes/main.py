from flask import Blueprint, render_template, jsonify

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def index():
    return render_template('index.html')

@main_bp.route('/health')
def health():
    return jsonify({'status': 'ok'})

@main_bp.route('/about')
def about():
    return render_template('about.html')