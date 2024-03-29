from flask import Flask
from config import config_options
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bootstrap import Bootstrap
from flask_bcrypt import Bcrypt

login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'

db=SQLAlchemy()
bootstrap = Bootstrap()
bcrypt = Bcrypt()

def create_app(config_name):
  app = Flask(__name__)

  #creating app configuarations
  app.config.from_object(config_options[config_name])

  #registering blueprints
  from .main import main as main_blueprint
  app.register_blueprint(main_blueprint)
  from .auth import auth as auth_blueprint
  app.register_blueprint(auth_blueprint)

  #initialising flask extensions
  db.init_app(app)
  login_manager.init_app(app)
  bootstrap.init_app(app)

  return app