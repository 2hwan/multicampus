from flask import Flask, render_template, request

app2 = Flask(__name__, template_folder='view')

@app2.route("/")
def index() :
    html = render_template('index.html')
    return html

@app2.route('/two', methods=['GET','POST'])
#get 은 url에 데이터를 붙여서 보내고 post는 body값에 데이터를 넣어서 보냄
def two():
    data3 = request.values.get('data2') #get, post 둘다 가능
    #요청 방식으로 분기
    if request.method == 'POST' :
        data1 = request.form['data1']
        data2 = request.form.get('data2')
        return f'data1 : {data1}, data2 :{data2}, data3 :{data3}'

    elif request.method == 'GET' :
        data1 = request.args['data1']
        data2 = request.args.get('data2') #없을 때 오류가 나나 안나냐
        return 'data1 : {0}, data2 : {1}, data3 : {2}'.format(data1,data2,data3)

    return 'Hello World'