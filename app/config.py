import os
SECRET_KEY = os.urandom(32)

import os


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'any_key'