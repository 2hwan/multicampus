from flask import Blueprint, render_template, request

blue100 = Blueprint('blue1', __name__, template_folder='templates/sub1')
# blue100 = Blueprint('blue1', __name__, url_prefix='/blue1', template_folder='templates/sub1')

@blue100.route('/test3')
def test3() :
    html = render_template('test2.html')
    return html