from flask import Flask
from app.routes import main
import os

def create_app():
    template_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), 'app', 'templates'))
    app = Flask(__name__, template_folder=template_dir)
    app.register_blueprint(main)
    return app

if __name__ == "__main__":
    app = create_app()
    app.run(host='0.0.0.0', port=8080)