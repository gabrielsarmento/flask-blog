import os
url = 'postgres://postgres:@localhost:5432/postgres'

class Config:
    SECRET_KEY = 'okgoogle'
    SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = 'username'
    MAIL_PASSWORD = 'password'
