from flask import Flask
from config import Config
from .models import db, login
from flask_migrate import Migrate
from .api.routes import api
from .auth.routes import auth
from flask_cors import CORS


app = Flask(__name__)
app.config.from_object(Config)
CORS(app, origins=['*'])
db.init_app(app)
migrate = Migrate(app, db)
app.register_blueprint(api)
app.register_blueprint(auth)
login.init_app(app)
login.login_view = 'auth.login'
login.login_message = 'Please log in to seet his page.'
login.login_message_category = 'danger'



from . import routes