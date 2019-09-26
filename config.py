import os
class Config:
  '''
  class that defines configuarations
  '''
  SECRET_KEY='7cf79c6a761ba6ae077394a44ddfc6b5'
  QUOTES_URL = 'http://quotes.stormconsultancy.co.uk/random.json'
  
class ProdConfig(Config):
  '''
  class that defines configuarations in production
  '''
  SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
  DEBUG=False

class DevConfig(Config):
  '''
  class that defines configuarations in development
  '''
  DEBUG=True
  SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://emmanuel:123456@localhost/blogs'

config_options = {
  'development' :DevConfig,
  'production'  :ProdConfig
}

