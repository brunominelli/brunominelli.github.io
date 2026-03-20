from flask import Flask

from src.modules.institutional.ui.routes import institutional

app = Flask(__name__)
app.secret_key = 'secret'
app.register_blueprint(blueprint=institutional)

if __name__ == '__main__':
    app.run(debug=True)