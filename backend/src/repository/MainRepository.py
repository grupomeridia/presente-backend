from flask import Flask
from flask_sqlalchemy import SQLAlchemy

class MainRepository():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@localhost/presente'
    db = SQLAlchemy(app)
