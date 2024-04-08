from db import db


class CityModel(db.Model):
    __tablename__ = 'cities'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    additional_info = db.Column(db.String(80), nullable=False)