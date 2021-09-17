# Settings common to all environments (development|staging|production)
import os


DEBUG = True

# Application settings
APP_NAME = "AssemblyAI take home"
APP_SYSTEM_ERROR_SUBJECT_LINE = APP_NAME + " system error"

# Flask settings
CSRF_ENABLED = True

# Flask-SQLAlchemy settings
SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://test:test@db/test'
#SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'

# Flask secret, yes it's not static
SECRET_KEY = os.urandom(16)

# Redis backend
REDIS_URL = 'redis://localhost:6379/1'
