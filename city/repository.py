from typing import List

from city.models import CityModel
from injector import inject


class CityRepository:
    @inject
    def __init__(self, session):
        self.session = session

    def get_all(self) -> List[CityModel]:
        return CityModel.query.all()

    def create(self, city) -> CityModel:
        model = CityModel(**city)
        self.session.add(model)
        self.session.commit()
        return model
