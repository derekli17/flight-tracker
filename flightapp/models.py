"""
Flight-Tracker model (database) API
"""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

class Flight(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    flight_number = db.Column(db.String(10), unique=True, nullable=False)
    max_price = db.Column(db.Float, nullable=False)

class Preference(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    flight_id = db.Column(db.Integer, db.ForeignKey('flight.id'), nullable=False)

    user = db.relationship('User', backref=db.backref('preferences', lazy=True))
    flight = db.relationship('Flight', backref=db.backref('preferences', lazy=True))

# Note: You might need to add additional fields, relationships, and methods to your models based on your requirements.
