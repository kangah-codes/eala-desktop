from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_session import Session
from flask_login import LoginManager
import os

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{os.getcwd()}/database.db"
app.config['SECRET_KEY'] = 'vnkdjnfjknfl1232#'
app.config['UPLOAD_FOLDER'] = os.getcwd()+'/static/uploads'
app.config['SESSION_TYPE'] = 'memcached'
sess = Session()
login = LoginManager(app)
login.init_app(app)
db = SQLAlchemy(app)
db.create_all()

from models import *

if __name__ == "__main__":
	from views import *
	app.run(debug=True)
