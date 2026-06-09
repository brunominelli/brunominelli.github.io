from app import App
from flask_frozen import Freezer

app = App().create_app()
app.config['TESTING'] = True 
app.config['PROPAGATE_EXCEPTIONS'] = True
freezer = Freezer(app=app)

if __name__ == "__main__":
    freezer.freeze()
    # app.run(debug=True)