import os


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'something_something_dark_side'
