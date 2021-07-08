from .api import bp
from flask import Flask


def init_app(app: Flask):
    app.register_blueprint(bp)
