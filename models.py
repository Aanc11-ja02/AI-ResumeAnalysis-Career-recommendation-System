import json
from datetime import datetime
from flask_login import UserMixin
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy()

class User(UserMixin, db.Model):
    __tablename__ = 'users'
    
    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False, index=True)
    password_hash = db.Column(db.String(256), nullable=False)
    is_admin = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # Relationships
    analyses = db.relationship('ResumeAnalysis', backref='user', lazy='dynamic', cascade='all, delete-orphan')

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return f'<User {self.email}>'


class ResumeAnalysis(db.Model):
    __tablename__ = 'resume_analyses'
    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    filename = db.Column(db.String(255), nullable=False)
    file_type = db.Column(db.String(10), nullable=False)
    file_size_kb = db.Column(db.Float, default=0.0)
    created_at = db.Column(db.DateTime, default=datetime.utcnow, index=True)
    
    # Analysis metrics
    overall_score = db.Column(db.Float, nullable=False, default=0.0)
    predicted_experience_level = db.Column(db.String(50), nullable=False, default='Fresher')
    years_of_experience_est = db.Column(db.Float, default=0.0)
    
    # Serialized JSON structures
    extracted_skills_json = db.Column(db.Text, nullable=False, default='{}')
    sections_json = db.Column(db.Text, nullable=False, default='{}')
    scoring_breakdown_json = db.Column(db.Text, nullable=False, default='{}')
    recommendations_json = db.Column(db.Text, nullable=False, default='[]')
    raw_text = db.Column(db.Text, nullable=True)

    @property
    def extracted_skills(self):
        try:
            return json.loads(self.extracted_skills_json)
        except Exception:
            return {'hard_skills': [], 'soft_skills': []}

    @extracted_skills.setter
    def extracted_skills(self, value):
        self.extracted_skills_json = json.dumps(value)

    @property
    def sections(self):
        try:
            return json.loads(self.sections_json)
        except Exception:
            return {}

    @sections.setter
    def sections(self, value):
        self.sections_json = json.dumps(value)

    @property
    def scoring_breakdown(self):
        try:
            return json.loads(self.scoring_breakdown_json)
        except Exception:
            return {}

    @scoring_breakdown.setter
    def scoring_breakdown(self, value):
        self.scoring_breakdown_json = json.dumps(value)

    @property
    def recommendations(self):
        try:
            return json.loads(self.recommendations_json)
        except Exception:
            return []

    @recommendations.setter
    def recommendations(self, value):
        self.recommendations_json = json.dumps(value)

    def __repr__(self):
        return f'<ResumeAnalysis {self.id} for User {self.user_id}>'
