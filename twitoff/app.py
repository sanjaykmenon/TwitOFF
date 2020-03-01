from flask import Flask
def create_app():
    """ Create and configure an instance of the Flask Application."""
    app = Flask(__name__)

    @app.route('/')
    def root():
        return 'HEllo TwitOff!'
    
    return app
