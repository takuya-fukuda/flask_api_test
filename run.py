import os

from flask import Flask

from .api import api
from .api.config import config
from flask_cors import CORS #javascriptでAPIたたくためにいれた

config_name = os.environ.get("CONFIG", "local")

app = Flask(__name__)

CORS(app) #javascriptたたく用こうしてるだけ

app.config.from_object(config[config_name])
# blueprintをアプリケーションに登録
app.register_blueprint(api)