from flask import Flask
from ext import config


def create_app():
    """Factory para criar um app Flask baseado no padrão factory"""
    app = Flask(__name__)
    config.init_app(app)
    return app

my_app = create_app()