import requests

from city.service import CityService
from temperature.repository import TemperatureRepository
from temperature.schema import TemperatureSchema


class TemperatureService:
    def __init__(self):
        self.temperature_repository = TemperatureRepository()
        self.city_service = CityService()

    def get_all(self):
        return self.temperature_repository.get_all()

    def create(self, temperature: TemperatureSchema) -> TemperatureSchema:
        return self.temperature_repository.create(temperature)

    def update_temp_for_cities(self):
        cities = self.city_service.get_all_cities()
        for city in cities:
            current_temp = self.fetch_temperature(city.name)
            self.temperature_repository.update(city.id, current_temp)


    @staticmethod
    def fetch_temperature(city: str) -> float:
        base_url = f"http://api.weatherapi.com/v1/current.json?key=255f4d1fac4148f18c884205242602&q={city}"

        response = requests.get(base_url)
        return response.json()['current']['temp_c']
