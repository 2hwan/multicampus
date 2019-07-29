from flask import  Flask, render_template
from day16_flask.blue1 import blue100
from day16_flask.blue2 import blue200

app = Flask(__name__, template_folder='templates')
app.register_blueprint(blue100)
app.register_blueprint(blue200)

@app.route('/')
def index() :
    return 'index page'