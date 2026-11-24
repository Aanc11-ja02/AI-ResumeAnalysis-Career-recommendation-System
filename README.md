# AI Resume Analysis and Career Recommendation System

<div align="center">

# 📄 ResumeAI
### *Analyze Your Resume. Discover Your Career.*

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Framework-Flask_3.x-black.svg)](https://flask.palletsprojects.com/)
[![Machine Learning](https://img.shields.io/badge/ML-scikit--learn-orange.svg)](https://scikit-learn.org/)
[![NLP](https://img.shields.io/badge/NLP-Sentence--Transformers%20%7C%20spaCy-green.svg)](https://www.sbert.net/)
[![License](https://img.shields.io/badge/License-MIT-purple.svg)](#license)

**A complete, modular, and production-ready web application for intelligent resume parsing, multi-factor scoring, experience level classification, and semantic career recommendations.**

*Built strictly using pure Machine Learning &amp; Empirical NLP techniques — 100% Free of Generative AI / LLM APIs.*

</div>

---

## 🌟 Overview

**ResumeAI** transforms traditional resume screening into an objective, data-driven science. By eliminating hallucinations and rate-limits of external LLMs, the platform leverages deterministic NLP pipelines, Random Forest classification, and semantic vector embeddings to evaluate candidate profiles and provide actionable career roadmaps.

### Key Capabilities

1. **Intelligent Document Parsing**
   - Seamless parsing of both **PDF** (`pdfplumber`) and **DOCX** (`python-docx`) files up to **5 MB**.
   - Automatic segmentation of 6 distinct resume sections: *Summary*, *Work Experience*, *Education*, *Skills*, *Projects*, and *Certifications*.
   - Contact info extraction (email, phone, LinkedIn, GitHub).
   - Full model transparency with collapsible raw extracted text inspection.

2. **Dual-Stream Skill Extraction**
   - Categorizes hundreds of technical **Hard Skills** across 9 domains (Programming, Web/Frontend, Backend, Databases, Cloud/DevOps, AI/ML, Mobile, Security, Architecture).
   - Identifies interpersonal **Soft Skills** (Leadership, Communication, Problem Solving, Adaptability, etc.).
   - Utilizes `spaCy` tokenization paired with a curated taxonomic database.

3. **ML Experience Level Classification**
   - Persisted `RandomForestClassifier` (trained with `scikit-learn` and saved via `joblib`).
   - Classifies candidates into 4 distinct career tiers: **Fresher**, **Junior**, **Mid-Level**, and **Senior**.
   - Extracts date intervals, employment tenures, graduation milestones, and seniority keywords.

4. **Multi-Factor Weighted Resume Scoring (0–100)**
   - **Skills Diversity & Relevance (35%)**: Evaluates technical breadth and soft skill coverage.
   - **Work Experience Depth (25%)**: Assesses active years, job progression, and seniority.
   - **Education & Academics (15%)**: Weighted scoring from doctorate/masters to undergraduate degrees.
   - **Demonstrated Projects (15%)**: Practical execution evidence and technical complexity.
   - **Certifications & Accreditations (10%)**: Industry credentials and certifications.

5. **Semantic Career Recommendation Engine**
   - Uses `sentence-transformers` (`all-MiniLM-L6-v2`) embeddings + **Cosine Similarity**.
   - Matches candidate profiles against 18 comprehensive tech career profiles.
   - Dynamic **Skill Gap Analysis**: Identifies matched skills, missing skills, and suggests **Priority Skills to Learn** for career progression.

6. **Instant Downloadable PDF Reports**
   - Clean, publication-quality executive reports generated on-the-fly using `ReportLab`.
   - Complete with visual score badges, factor breakdowns, skill matrix, and career roadmaps.

7. **Authentication & User Management**
   - Secure registration, login, and logout powered by `Flask-Login` and `Werkzeug` SHA-256 password hashing.
   - Profile management (name and email updates) and password change functionality.
   - Personalized user dashboard with analysis history, score trends, and quick deletion.
   - Basic Admin Control Panel for administrative metrics and user management.

---

## 📁 Project Structure

```text
RESUME AI/
├── app/
│   ├── __init__.py              # Flask app factory, extension setup & error handlers
│   ├── config.py                # Configuration classes (Dev, Prod, Test)
│   ├── forms.py                 # Flask-WTF form classes
│   ├── models.py                # SQLAlchemy models: User and ResumeAnalysis
│   ├── routes/
│   │   ├── __init__.py
│   │   ├── admin.py             # Admin dashboard & management routes
│   │   ├── analysis.py          # Upload, analyze, result, history & PDF routes
│   │   ├── auth.py              # Register, login, logout, profile & password routes
│   │   └── main.py              # Home, dashboard & about routes
│   ├── services/
│   │   ├── __init__.py
│   │   ├── career_recommender.py# Sentence-Transformers embeddings & Cosine Similarity
│   │   ├── ml_models.py         # RandomForest classifier & weighted 0-100 scoring
│   │   ├── report_generator.py  # ReportLab PDF report generation
│   │   ├── resume_parser.py     # PDF & DOCX extraction & section segmenter
│   │   └── skill_extractor.py   # spaCy NLP & dual-stream skill extraction
│   ├── templates/
│   │   ├── base.html            # Main template with navbar, branding & footer
│   │   ├── index.html           # Landing page with hero, features & workflow
│   │   ├── dashboard.html       # Personalized user dashboard & score chart
│   │   ├── about.html           # Technical architecture of the ML engine
│   │   ├── admin/
│   │   │   └── dashboard.html   # Admin panel metrics & user list
│   │   ├── analysis/
│   │   │   ├── history.html     # User's complete analysis history table
│   │   │   ├── result.html      # Comprehensive report, skill gap & recommendations
│   │   │   └── upload.html      # Drag & drop upload with live processing modal
│   │   ├── auth/
│   │   │   ├── change_password.html
│   │   │   ├── login.html
│   │   │   ├── profile.html
│   │   │   └── register.html
│   │   └── errors/
│   │       ├── 403.html
│   │       ├── 404.html
│   │       ├── 413.html
│   │       └── 500.html
│   ├── static/
│   │   ├── css/
│   │   │   └── style.css        # Responsive styling & color palette
│   │   └── js/
│   │       └── main.js          # Client-side validation, drag-and-drop & loader
│   ├── data/
│   │   ├── careers.json         # 18 comprehensive tech career profiles
│   │   └── skills_db.json       # Categorized database of hard & soft skills
│   └── utils/
│       ├── __init__.py
│       └── helpers.py           # Filename & size format helpers
├── models/                      # Saved ML models (experience_model.joblib)
├── samples/                     # Ready-to-use sample resumes (PDF & DOCX)
├── uploads/                     # Upload storage directory
├── requirements.txt             # Dependency specification
├── run.py                       # Main application runner
└── README.md                    # Detailed documentation
```

---

## 🚀 Getting Started

### 1. Prerequisites
- Python 3.10+ (compatible with Python 3.10, 3.11, 3.12, 3.13, 3.14)
- Git

### 2. Clone the Repository
```bash
git clone <repository-url>
cd "RESUME AI"
```

### 3. Set Up a Virtual Environment (Recommended)
```bash
python -m venv venv

# Windows (Command Prompt / PowerShell)
.\venv\Scripts\activate

# macOS / Linux
source venv/bin/activate
```

### 4. Install Dependencies
```bash
pip install -r requirements.txt
```

*(Optional)* Download the spaCy English model for extended NLP parsing:
```bash
python -m spacy download en_core_web_sm
```
> **Note:** If `en_core_web_sm` is not downloaded, ResumeAI automatically falls back to spaCy's built-in English tokenizer, ensuring zero interruption.

### 5. Initialize the Database & ML Models
```bash
flask --app run.py init-db
```
This will create SQLite tables and pre-train the Random Forest experience classifier into `models/experience_model.joblib`.

### 6. Run the Application
```bash
python run.py
```
Open your web browser and navigate to:
```
http://127.0.0.1:5000
```

---

## 🔒 Default Admin Account

The **first user** to register on a clean database is automatically granted **Administrator** privileges (`is_admin = True`).
Administrators have access to:
- `/admin/` control center
- Global user overview
- Platform-wide analysis records
- Administrative role assignment

---

## 🧪 Testing with Sample Resumes

We include sample resumes in the `samples/` directory for immediate testing:
- `samples/Alex_Morgan_FullStack_Resume.pdf` (Mid-Level Full Stack Developer)
- `samples/Sarah_Chen_DataScientist_Resume.docx` (Mid-Senior Data Scientist)

To generate or refresh sample resumes, run:
```bash
python scratch/generate_samples.py
```

---

## 📊 Evaluation & Scoring Rubric

| Dimension | Max Points | Evaluation Methodology |
| :--- | :---: | :--- |
| **Skills Relevance** | 35 pts | Evaluates hard skills across 9 technical categories + demonstrated soft skills |
| **Experience Depth** | 25 pts | Analyzes explicit years, verified temporal dates, and role progression |
| **Education** | 15 pts | Ordinal qualification score (PhD: 10, Master: 8.5, Bachelor: 7, Diploma: 5) |
| **Projects** | 15 pts | Quantified practical project entries and action verbs |
| **Certifications** | 10 pts | Verified cloud, DevOps, security, or domain-specific credentials |
| **Polish Bonus** | +2 pts | Presence of executive summary / structured career objective |
| **Total Score** | **100 pts** | Combined composite resume health rating |

---

## 🛡️ Security & Quality Standards

- **Strict Size Caps**: Files strictly validated to `<= 5 MB` client-side and server-side.
- **CSRF Protection**: All forms guarded by `Flask-WTF` CSRF tokens.
- **Password Security**: Passwords hashed using Werkzeug `scrypt`/`pbkdf2` cryptographic standards.
- **Protected Endpoints**: `@login_required` decorators ensure authentication integrity.
- **Ownership Verification**: Users can only inspect and delete their own analysis reports.

---

## 📄 License

This project is licensed under the MIT License.
