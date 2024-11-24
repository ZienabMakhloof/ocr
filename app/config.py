import os

class Config:

    PERMANENT_SESSION_LIFETIME = 600  # 10 دقائق
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'your-secret-key'
    UPLOAD_FOLDER = 'instance/uploads'
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # 16MB max file size