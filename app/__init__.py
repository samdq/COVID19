# app/__init__.py



app = Flask(__name__)
app.config.from_object(Config)

from app import routes