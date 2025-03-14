from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False, unique=True)
    tasks = db.relationship('Task', backref='category', lazy=True)

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    status = db.Column(db.String(50), default='pending')
    created = db.Column(db.DateTime, default=datetime.utcnow)  # Cột created
    finished = db.Column(db.DateTime, nullable=True)  # Cột finished
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'), nullable=True)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), nullable=False, unique=True)
    password = db.Column(db.String(200), nullable=False)
    avatar = db.Column(db.String(200), nullable=True)  # Lưu đường dẫn avatar
    role = db.Column(db.String(50), default='user')
