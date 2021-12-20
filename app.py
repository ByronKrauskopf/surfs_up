#import dependencies
from flask import Flask

#Create new Flask instance
app = Flask(__name__)

#Create Flask route
@app.route('/')
def hello_world():
    return 'Hello world'

@app.route('/test')
def test():
    return 'This is a test'