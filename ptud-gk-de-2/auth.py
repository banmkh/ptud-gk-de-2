from flask import Blueprint, render_template, request, redirect, url_for, session, flash
from models import db
from werkzeug.security import generate_password_hash, check_password_hash

auth = Blueprint('auth', __name__)
from models import db, User
from werkzeug.security import generate_password_hash, check_password_hash

@auth.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        
        if User.query.filter_by(username=username).first():
            flash('Username already exists', 'danger')
            return redirect(url_for('auth.register'))
        
        hashed_password = generate_password_hash(password)
        new_user = User(username=username, password=hashed_password, role="user")
        db.session.add(new_user)
        db.session.commit()

        flash('Registration successful!', 'success')
        return redirect(url_for('auth.login'))
    
    return render_template('register.html')

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if 'user' in session:
        return redirect(url_for('routes.index'))

    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        user = User.query.filter_by(username=username).first()
        if user and check_password_hash(user.password, password):
            session['user'] = user.username
            session['role'] = user.role
            session['user_id'] = user.id  # Để hiển thị avatar
            flash('Login successful!', 'success')
            return redirect(url_for('routes.index'))
        
        flash('Invalid username or password', 'danger')

    return render_template('login.html')

@auth.route('/logout')
def logout():
    session.pop('user', None)
    session.pop('role', None)
    session.pop('user_id', None)
    flash('Logged out successfully', 'info')
    return redirect(url_for('auth.login'))