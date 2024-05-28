from decouple import config
from flask import Flask
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api
from src.user.services.user import RegisterUser

app = Flask(__name__)
app.config.from_object(config("APP_SETTINGS"))

login_manager = LoginManager()
login_manager.init_app(app)

bcrypt = Bcrypt(app)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
api = Api(app)

# Registering blueprints

from src.tasks.views.view import task
from src.user.views.view import user


app.register_blueprint(task)
app.register_blueprint(user)


from src.user.models.user_model import User


# Routes
api.add_resource(RegisterUser, '/RegisterUser')