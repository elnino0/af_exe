from flask import Flask
from app.routes import scanMockRouter

def create_app():
    app = Flask(__name__, instance_relative_config=True)
    app.register_blueprint(scanMockRouter.bp)
    
    return app