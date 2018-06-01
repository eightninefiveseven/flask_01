from flask import Blueprint
apd = Blueprint('apd',__name__)

@apd.route('/list-4')
def list():
    return 'list-4'

@apd.route('/detail-4')
def detail():
    return 'detail-4'