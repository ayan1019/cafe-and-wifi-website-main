from flask import Flask
from flask_bootstrap import Bootstrap5
from dotenv import load_dotenv
from flask_ckeditor import CKEditor
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase
from flask_migrate import Migrate
import os
from dotenv import load_dotenv

load_dotenv("/Users/ayan/Downloads/cafe-and-wifi-website-main/environ.env")

class Base(DeclarativeBase):
    pass


app = Flask(__name__)

load_dotenv()
app.config['SECRET_KEY'] = os.getenv("API_KEY")
Bootstrap5(app)
ckeditor = CKEditor(app)

db = SQLAlchemy(model_class=Base)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
db.init_app(app)
migrate = Migrate(app, db)

login_manager = LoginManager()
login_manager.init_app(app)

from app import routes, models
