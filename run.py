import os
from app import create_app
from app.models import db, User
from app.services.ml_models import get_experience_model

app = create_app(os.environ.get('FLASK_CONFIG', 'development'))

@app.cli.command("init-db")
def init_db():
    """Initializes the database tables and pre-trains the ML model."""
    with app.app_context():
        db.create_all()
        print("[OK] Database tables created successfully.")
        
        # Pre-train and persist Random Forest model
        try:
            model = get_experience_model()
            if model is not None:
                print("[OK] Experience prediction RandomForestClassifier persisted to models/experience_model.joblib.")
        except Exception as e:
            print(f"[NOTE] Model training notice: {e}")

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    print(f"\n=======================================================")
    print(f"  ResumeAI - AI-Based Resume Analysis System")
    print(f"  Analyze Your Resume. Discover Your Career.")
    print(f"  Starting server at: http://127.0.0.1:{port}")
    print(f"=======================================================\n")
    app.run(host='0.0.0.0', port=port, debug=True)
