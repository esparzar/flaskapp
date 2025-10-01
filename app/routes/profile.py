import os
from flask import Blueprint, render_template, flash, redirect, url_for, request, current_app
from flask_login import login_required, current_user
from werkzeug.utils import secure_filename
from app.models import User, Blog
from app import db

profile_bp = Blueprint('profile', __name__)

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in current_app.config['ALLOWED_EXTENSIONS']

from flask import Blueprint, render_template, flash, redirect, url_for, request
from flask_login import login_required, current_user
from app.models import User, Blog
from app import db

profile_bp = Blueprint('profile', __name__)

@profile_bp.route('/profile/<username>')
def view_profile(username):
    user = User.query.filter_by(username=username).first_or_404()
    posts = user.posts.order_by(Blog.created_at.desc()).limit(5).all()
    return render_template('profile/view.html', user=user, posts=posts)

@profile_bp.route('/profile/edit', methods=['GET', 'POST'])
@login_required
def edit_profile():
    if request.method == 'POST':
        current_user.full_name = request.form.get('full_name')
        current_user.bio = request.form.get('bio')
        current_user.location = request.form.get('location')
        current_user.website = request.form.get('website')
        
        # Update avatar if provided
        avatar = request.files.get('avatar')
        if avatar and allowed_file(avatar.filename):
            filename = secure_filename(avatar.filename)
            avatar.save(os.path.join(current_app.config['UPLOAD_FOLDER'], filename))
            current_user.avatar_url = filename
        
        db.session.commit()
        flash('Your profile has been updated!', 'success')
        return redirect(url_for('profile.view_profile', username=current_user.username))
    
    return render_template('profile/edit.html')