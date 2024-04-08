import datetime
from db import db


class TemperatureModel(db.Model):
    __tablename__ = 'temperature'

    id = db.Column(db.Integer, primary_key=True)
    temperature = db.Column(db.Double, nullable=False)
    datetime = db.Column(db.DateTime, nullable=False, default=datetime.datetime.now())
    city_id = db.Column(db.Integer, db.ForeignKey('cities.id'), nullable=False)
