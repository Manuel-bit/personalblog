import os
class Config:
  '''
  class that defines configuarations
  '''
  SECRET_KEY='7cf79c6a761ba6ae077394a44ddfc6b5'
  
class ProdConfig(Config):
  '''
  class that defines configuarations in production
  '''
  SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
  

class DevConfig(Config):
  '''
  class that defines configuarations in development
  '''
  DEBUG=True

config_options = {
  'development' :DevConfig,
  'production'  :ProdConfig
}

