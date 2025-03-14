from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from models import db, Task,Category
import os
from functools import wraps

routes = Blueprint('routes', __name__)
UPLOAD_FOLDER = 'static/avatars'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user' not in session:
            flash('You must be logged in to access this page', 'danger')
            return redirect(url_for('auth.login'))
        return f(*args, **kwargs)
    return decorated_function

@routes.route('/')
@login_required
def index():
    category_id = request.args.get('category_id', type=int)  # Lấy category từ query string
    categories = Category.query.all()
    
    if category_id:
        tasks = Task.query.filter_by(category_id=category_id).all()
    else:
        tasks = Task.query.all()

    return render_template('index.html', tasks=tasks, categories=categories, selected_category=category_id)


@routes.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        if username and password:
            # Giả lập lưu user vào session (thay bằng database sau này)
            session['user'] = username
            session['role'] = 'user'
            flash('Registration successful! Please log in.', 'success')
            return redirect(url_for('auth.login'))
        flash('Please enter a valid username and password', 'danger')
    return render_template('register.html')

@routes.route('/categories', methods=['GET', 'POST'])
@login_required
def manage_categories():
    if request.method == 'POST':
        category_name = request.form.get('category_name')
        if category_name:
            new_category = Category(name=category_name)
            db.session.add(new_category)
            db.session.commit()
            flash('Category added successfully!', 'success')
    categories = Category.query.all()
    return render_template('categories.html', categories=categories)

@routes.route('/add_task', methods=['POST'])
@login_required
def add_task():
    task_name = request.form.get('task_name')
    category_id = request.form.get('category_id')

    if task_name:
        new_task = Task(name=task_name, category_id=category_id if category_id else None)
        db.session.add(new_task)
        db.session.commit()
        flash('Task added successfully!', 'success')

    return redirect(url_for('routes.index'))



@routes.route('/delete/<int:task_id>', methods=['POST'])
@login_required
def delete_task(task_id):
    task = Task.query.get(task_id)
    if task:
        db.session.delete(task)
        db.session.commit()
        flash('Task deleted successfully!', 'success')
    return redirect(url_for('routes.index'))

@routes.route('/update/<int:task_id>', methods=['POST'])
@login_required
def update_task(task_id):
    task = Task.query.get(task_id)
    if task:
        task.status = request.form.get('status', task.status)
        db.session.commit()
        flash('Task updated successfully!', 'success')
    return redirect(url_for('routes.index'))

@routes.route('/upload_avatar', methods=['POST'])
@login_required
def upload_avatar():
    if 'avatar' not in request.files:
        flash('No file part', 'danger')
        return redirect(url_for('routes.index'))
    file = request.files['avatar']
    if file.filename == '':
        flash('No selected file', 'danger')
        return redirect(url_for('routes.index'))
    file_path = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(file_path)
    flash('Avatar uploaded successfully!', 'success')
    return redirect(url_for('routes.index'))

