from demo_02 import apb

@apb.route('/list-3')
def list():
    return 'list-3'

@apb.route('/detail-3')
def detail():
    return 'detail-3'