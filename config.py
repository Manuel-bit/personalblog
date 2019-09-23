class Config:
  '''
  class that defines configuarations
  '''
  SECRET_KEY='7cf79c6a761ba6ae077394a44ddfc6b5'
  SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://emmanuel:123456@localhost/blogs'

class ProdConfig(Config):
  '''
  class that defines configuarations in production
  '''
  pass

class DevConfig(Config):
  '''
  class that defines configuarations in development
  '''
  DEBUG=True

config_options = {
  'development' :DevConfig,
  'production'  :ProdConfig
}

