__author__ = 'enzyme'
__date__ = '2019/4/12 2:27 PM'

from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello, World!'
