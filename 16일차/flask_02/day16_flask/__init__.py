import json
from flask import Flask, render_template

app = Flask(__name__, template_folder='templates')

test_dic = {
        'a1' : 100,
        'a2' : '문자열'
    }
test_list = (10, 20, 30, 40, 50)

@app.route("/")
def index() :


    html = render_template('index.html', data_dic = test_dic, data_list=test_list)
    return html

@app.route("/testjson")
def testjson():
    json_data = json.dumps(test_dic, indent=4, ensure_ascii=False)
    print(type(json_data), json_data)

    python_data = json.loads(json_data)
    print(type(python_data), python_data)

    return json_data

@app.route('/test1')
def test1():
    return 'test1'

@app.route('/test1/sub1')
def test1_sub1() :
    return 'test1 sub1'

@app.route('/user/<username>/<int:age>') #형변환
def show_user_profile_age(username, age):
    return 'Username %s, 나이 %d' % (username,age)

