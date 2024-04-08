from typing import List

from city.models import CityModel
from city.repository import CityRepository
from city.schema import CitySchema


class CityService:
    def __init__(self):
        self.city_repository = CityRepository()

    def get_all_cities(self) -> List[CitySchema]:
        return self.city_repository.get_all()

    def create_city(self, city: CitySchema) -> CitySchema:
        return self.city_repository.create(city)
