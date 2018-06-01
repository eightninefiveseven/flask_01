from flask import Blueprint
apb = Blueprint('apb',__name__)
from demo_03 import apb
@apb.route('/edit')
def edit():
    return 'edit'

@apb.route('/publish')
def publish():
    return 'publish'