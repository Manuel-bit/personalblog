from flask import Flask
from config import config_options
from flask_sqlalchemy import SQLAlchemy

db=SQLAlchemy()

def create_app(config_name):
  app = Flask(__name__)

  #creating app configuarations
  app.config.from_object(config_options[config_name])

  #registering blueprints
  from .main import main as main_blueprint
  app.register_blueprint(main_blueprint)

  #initialising flask extensions
  db.init_app(app)

  return app