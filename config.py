import os

class Config:
    """This are the configurations for the entire app in every environment
    """
    SECRET_KEY = os.environ.get('SECRET_KEY')
    UPLOADED_PHOTOS_DEST ='app/static/photos'
    QUOTES_URL = os.environ.get('QUOTE_URL')

class DevConfig(Config):
    """This are the configurations for the development environment
    Args:
        Config ([type]): [description]
    """
    DEBUG=True
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://kenmbira:1234@localhost/bloggy'
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")

class ProdConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")

class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://kenmbira:1234@localhost/blogspot_test'
    

config_options = {
    'development':DevConfig,
    'production':ProdConfig,
    'test':TestConfig
}
