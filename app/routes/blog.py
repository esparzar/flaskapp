from flask import render_template, flash, redirect, url_for, request
from flask_login import login_required, current_user
from app.routes import blog_bp
from app.models import Blog
from app import db

@blog_bp.route('/blog')
def index():
    page = request.args.get('page', 1, type=int)
    posts = Blog.query.order_by(Blog.created_at.desc()).paginate(page=page, per_page=10)
    return render_template('blog/index.html', posts=posts)

@blog_bp.route('/blog/create', methods=['GET', 'POST'])
@login_required
def create():
    if request.method == 'POST':
        title = request.form.get('title')
        content = request.form.get('content')
        
        post = Blog(title=title, content=content, author=current_user)
        db.session.add(post)
        db.session.commit()
        
        flash('Your post has been created!', 'success')
        return redirect(url_for('blog.index'))
    
    return render_template('blog/create.html')

@blog_bp.route('/blog/<int:id>')
def view(id):
    post = Blog.query.get_or_404(id)
    return render_template('blog/view.html', post=post)

@blog_bp.route('/blog/<int:id>/edit', methods=['GET', 'POST'])
@login_required
def edit(id):
    post = Blog.query.get_or_404(id)
    if post.author != current_user:
        flash('You can only edit your own posts!', 'danger')
        return redirect(url_for('blog.index'))
    
    if request.method == 'POST':
        post.title = request.form.get('title')
        post.content = request.form.get('content')
        db.session.commit()
        
        flash('Your post has been updated!', 'success')
        return redirect(url_for('blog.view', id=post.id))
    
    return render_template('blog/edit.html', post=post)