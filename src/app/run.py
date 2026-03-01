from flask import Flask
from src.modules.institutional.ui.routes import institutional

def create_app():
    app = Flask(__name__)
    app.secret_key = 'secret'
    app.register_blueprint(institutional)
    return app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)