from . import db, login_manager
from flask_login import UserMixin
from datetime import datetime

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(60), nullable=False)
    role = db.Column(db.String(20), nullable=False, default='detective')
    xp = db.Column(db.Integer, default=0)
    rank = db.Column(db.String(50), default='Rookie')
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    
    progress = db.relationship('UserProgress', backref='detective', lazy=True)

class Case(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    difficulty = db.Column(db.String(20), nullable=False)
    is_published = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    
    evidence = db.relationship('Evidence', backref='case', lazy=True)
    suspects = db.relationship('Suspect', backref='case', lazy=True)
    clues = db.relationship('Clue', backref='case', lazy=True)
    timeline_events = db.relationship('TimelineEvent', backref='case', lazy=True)

class UserProgress(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    case_id = db.Column(db.Integer, db.ForeignKey('case.id'), nullable=False)
    status = db.Column(db.String(20), nullable=False, default='unlocked') # unlocked, in_progress, solved, failed
    score = db.Column(db.Integer, default=0)
    started_at = db.Column(db.DateTime, nullable=True)
    completed_at = db.Column(db.DateTime, nullable=True)

class Evidence(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    case_id = db.Column(db.Integer, db.ForeignKey('case.id'), nullable=False)
    name = db.Column(db.String(100), nullable=False)
    type = db.Column(db.String(50), nullable=False) # document, physical, photo, digital
    description = db.Column(db.Text, nullable=False)
    image_url = db.Column(db.String(255), nullable=True)
    unlock_condition = db.Column(db.String(255), nullable=True) # json logic or simple flag

class Suspect(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    case_id = db.Column(db.Integer, db.ForeignKey('case.id'), nullable=False)
    name = db.Column(db.String(100), nullable=False)
    profile = db.Column(db.Text, nullable=False)
    image_url = db.Column(db.String(255), nullable=True)

class InterviewNode(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    suspect_id = db.Column(db.Integer, db.ForeignKey('suspect.id'), nullable=False)
    question = db.Column(db.Text, nullable=False)
    answer = db.Column(db.Text, nullable=False)
    unlocks_evidence_id = db.Column(db.Integer, db.ForeignKey('evidence.id'), nullable=True)
    requires_evidence_id = db.Column(db.Integer, db.ForeignKey('evidence.id'), nullable=True)

class Clue(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    case_id = db.Column(db.Integer, db.ForeignKey('case.id'), nullable=False)
    description = db.Column(db.Text, nullable=False)
    type = db.Column(db.String(50), nullable=False) # location, motive, weapon

class TimelineEvent(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    case_id = db.Column(db.Integer, db.ForeignKey('case.id'), nullable=False)
    time = db.Column(db.String(50), nullable=False)
    event_description = db.Column(db.Text, nullable=False)
