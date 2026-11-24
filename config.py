import os

BASE_DIR = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY', 'resume-ai-production-super-secret-key-2026')
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        'DATABASE_URL', f"sqlite:///{os.path.join(BASE_DIR, 'resume_ai.db')}"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    # 5 MB maximum file upload size
    MAX_CONTENT_LENGTH = 5 * 1024 * 1024
    
    UPLOAD_FOLDER = os.path.join(BASE_DIR, 'uploads')
    DATA_FOLDER = os.path.join(BASE_DIR, 'app', 'data')
    MODELS_FOLDER = os.path.join(BASE_DIR, 'models')
    
    ALLOWED_EXTENSIONS = {'pdf', 'docx'}
    
    # WTForms CSRF
    WTF_CSRF_ENABLED = True
    WTF_CSRF_TIME_LIMIT = 3600

class DevelopmentConfig(Config):
    DEBUG = True

class ProductionConfig(Config):
    DEBUG = False

config_by_name = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}
