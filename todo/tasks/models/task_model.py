from app import db
import uuid
from sqlalchemy import String
from datetime import datetime

class Task(db.Model):
    """Tasks"""
    __tablename__ = "task"

    id = db.Column(db.integer, primary_key=True, autoincrement=True)
    uuid = db.Column(String(36), unique=True, nullable=False, default=uuid.uuid4)
    task_name = db.Column(db.String, nullable=False)
    description =db.Column(db.String, nullable=False)
    start_date = db.Column(db.DateTime, nullable=False)
    end_date = db.Column(db.DateTime, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    modified_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow, onupdate=datetime.utcnow)

    # lINKS
    link_user =db.Column(db.String(36), nullable=False, index=True)
    
    def __repr__(self):
        return self.name
