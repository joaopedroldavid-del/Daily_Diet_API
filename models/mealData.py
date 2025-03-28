from database import db
from datetime import datetime

class Meal (db.Model):
    id = db.Column(db.Integer, primary_key=True)
    food = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(255), nullable=False)
    timetable = db.Column(db.DateTime, nullable=False, default=datetime)
    fl_diet = db.Column(db.Boolean, nullable=False)