from flask import Flask, session
from models import db
from routes import routes
from auth import auth
import os

app = Flask(__name__)
app.secret_key = 'supersecretkey'  # Đổi khóa này trong môi trường thật
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
app.register_blueprint(routes)
app.register_blueprint(auth, url_prefix='/auth')

def create_database():
    """ Tạo database nếu chưa tồn tại """
    if not os.path.exists("database.db"):
        with app.app_context():
            db.create_all()
        print("Created database!")

if __name__ == '__main__':
    create_database()  # Đảm bảo database được tạo
    app.run(debug=True)
