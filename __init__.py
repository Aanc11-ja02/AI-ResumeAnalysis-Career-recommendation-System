import os
from flask import Flask, render_template
from flask_login import LoginManager
from flask_wtf.csrf import CSRFProtect
from app.config import config_by_name
from app.models import db, User

login_manager = LoginManager()
login_manager.login_view = 'auth.login'
login_manager.login_message = 'Please log in to access this page.'
login_manager.login_message_category = 'warning'

csrf = CSRFProtect()

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

def create_app(config_name='development'):
    app = Flask(__name__)
    app.config.from_object(config_by_name[config_name])

    # Ensure necessary directory paths exist
    os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
    os.makedirs(app.config['MODELS_FOLDER'], exist_ok=True)
    os.makedirs(app.config['DATA_FOLDER'], exist_ok=True)

    # Initialize extensions
    db.init_app(app)
    login_manager.init_app(app)
    csrf.init_app(app)

    # Register blueprints
    from app.routes.auth import auth_bp
    from app.routes.main import main_bp
    from app.routes.analysis import analysis_bp
    from app.routes.admin import admin_bp

    app.register_blueprint(auth_bp)
    app.register_blueprint(main_bp)
    app.register_blueprint(analysis_bp)
    app.register_blueprint(admin_bp)

    # Template context variables for unified branding across all pages
    @app.context_processor
    def inject_branding():
        return {
            'app_title': 'AI Resume Analysis and Career Recommendation System',
            'website_name': 'ResumeAI',
            'tagline': 'Analyze Your Resume. Discover Your Career.'
        }

    # Custom Error Handlers
    @app.errorhandler(404)
    def page_not_found(e):
        return render_template('errors/404.html'), 404

    @app.errorhandler(403)
    def forbidden(e):
        return render_template('errors/403.html'), 403

    @app.errorhandler(413)
    def request_entity_too_large(e):
        return render_template('errors/413.html'), 413

    @app.errorhandler(500)
    def internal_server_error(e):
        return render_template('errors/500.html'), 500

    # Initialize database tables
    with app.app_context():
        db.create_all()

    return app
