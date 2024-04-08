from flask.views import MethodView
from flask_smorest import Blueprint

from temperature.schema import TemperatureSchema
from temperature.service import TemperatureService

blp = Blueprint('Temperatures', __name__, url_prefix='/temperature')


@blp.route('/')
class TemperatureView(MethodView):
    def __init__(self):
        self.service = TemperatureService()

    @blp.response(200, TemperatureSchema(many=True))
    def get(self):
        return self.service.get_all()

    @blp.response(200)
    def post(self):
        return self.service.update_temp_for_cities()
