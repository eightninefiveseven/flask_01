from flask import Flask
from flask import Blueprint

app=Flask(__name__)
api = Blueprint('api',__name__)
from demo_02 import api
@api.route('/')
def index():
    return 'index'

@api.route('/list')
def list():
    return 'list'

@api.route('/detail')
def detail():
    return 'detail'

if __name__=='__main__':
    app.run()