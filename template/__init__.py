import os

from flask import Flask

def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)


    @app.route('/healthz')
    def healthz():
        return 'ok'

    return app