import os

url = os.environ.get('DATABASE_URL')
if not url:
    url = 'postgres://postgres:root@localhost:5432/postgres'

class Config:
    SECRET_KEY = 'okgoogle'
    SQLALCHEMY_DATABASE_URI = url
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = 'username'
    MAIL_PASSWORD = 'password'
