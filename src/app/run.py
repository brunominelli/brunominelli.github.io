from flask import Flask

def create_app():
    app = Flask(__name__)
    app.secret_key = 'secret'
    return app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)