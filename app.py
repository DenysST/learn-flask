from flask import Flask
from flask_smorest import Api
from city.view import blp as CityBlueprint
from temperature.view import blp as TemperatureBlueprint
from db import db
from flask_migrate import Migrate
import city.models
import temperature.models

app = Flask(__name__)

app.config["PROPAGATE_EXCEPTIONS"] = True
app.config["API_TITLE"] = "First app"
app.config["API_VERSION"] = "v1"
app.config["OPENAPI_VERSION"] = "3.0.0"
app.config["OPENAPI_URL_PREFIX"] = "/"
app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdnjs.cloudflare.com/ajax/libs/swagger-ui/3.24.2/"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)
migrate = Migrate(app, db)

api = Api(app)

api.register_blueprint(CityBlueprint)
api.register_blueprint(TemperatureBlueprint)

if __name__ == '__main__':
    app.run(debug=True)
