from flask import Flask

apa = Flask(__name__)
from demo_02 import apb
apa.register_blueprint(apb)
from demo_04 import apd
apa.register_blueprint(apd)
@apa.route('/')
def index():
    return 'index'

@apa.route('/list-1')
def list():
    return 'list-1'

@apa.route('/detail-1')
def detail():
    return 'detail-1'

if __name__ == '__main__':
    apa.run()
