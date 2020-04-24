from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from app import db,app

db = SQLAlchemy(app)

class Message(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(20))
    body = db.Column(db.String(200))
    timestamp = db.Column(db.DateTime,default=datetime.utcnow,index=True)
