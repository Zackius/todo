from app import db
import uuid
from sqlalchemy import String
from datetime import datetime

class User(db.Model):
    """Todo Users"""
    __tablename__ = "user"

    id = db.Column(db.integer, primary_key=True, autoincrement=True)
    uuid = db.Column(String(36), unique=True, nullable=False, default=uuid.uuid4)
    full_name = db.Column(db.String, nullable=False)
    user_name = db.Column(db.String, nullable=False, unique=True)
    email = db.Column(db.VARCHAR, nullable=True, unique=True)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    modified_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow, onupdate=datetime.utcnow)
    password = db.Column(db.VARCHAR, nullable=False, unique=True)

    def __repr__(self):
        return self.name


    


