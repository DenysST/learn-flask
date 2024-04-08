from flask_smorest import Blueprint
from flask.views import MethodView

from city.schema import CitySchema
from city.service import CityService

blp = Blueprint("Cities", __name__, url_prefix="/city")


@blp.route("/")
class CityView(MethodView):
    @blp.response(200, CitySchema(many=True))
    def get(self):
        city_service = CityService()
        return city_service.get_all_cities()

    @blp.arguments(CitySchema)
    @blp.response(200, CitySchema)
    def post(self, city_data):
        city_service = CityService()
        return city_service.create_city(city_data)
