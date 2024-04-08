from typing import List

from db import db
from temperature.models import TemperatureModel


class TemperatureRepository:
    def __init__(self):
        self.session = db.session

    def get_all(self) -> List[TemperatureModel]:
        return TemperatureModel.query.all()

    def get_by_city_id(self, city_id: int) -> TemperatureModel:
        return TemperatureModel.query.filter_by(city_id=city_id).first()

    def update(self, city_id: int, temperature) -> None:
        temperature_from_db = self.get_by_city_id(city_id)
        if temperature_from_db:
            temperature_from_db.temperature = temperature
            self.session.add(temperature_from_db)
            self.session.commit()
        else:
            new_temperature = TemperatureModel(city_id=city_id, temperature=temperature)
            self.create(new_temperature)

    def create(self, temperature: TemperatureModel) -> TemperatureModel:
        self.session.add(temperature)
        self.session.commit()
        return temperature
