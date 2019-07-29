from flask import Flask, render_template, request

app = Flask(__name__, template_folder='view')

@app.before_first_request #이벤트 5개
def before_first_request(): #db 오픈
    print('before_first_request, 앱 기동하고 맨처음 요청만 응답')

@app.before_request
def before_request():
    print('before_request, 모든 요청에대해 응답, view함수')

@app.after_request
def after_request(response):
    print('after_request,매 요청 처리되고 나서, 브라우저에 응답하기 전 실행')
    return(response)

@app.teardown_request #db 클로즈
def teardown_request(exception):
    print('teardown_request,브라우저에 응답한 다음 실행')
    return exception

@app.teardown_appcontext
def teardown_appcontext(exception):
    print('teardown_appcontext, 요청이 완전히 끝나고 app_context 블록안에서 사용된 객체를 제거할 때 사용')
    return exception

# @app.route('/', methods=['GET','POST'])
# def helloword():
#     # return "Hello World"
#     return render_template('one.html', name='홍길동')

@app.route('/') # GET 생략 하이퍼 링크는 get 방식, summit이 들어가는게 post
def one():
    html = render_template('one.html')
    return html

@app.route('/two', methods=['GET','POST'])
def two():
    #요청 방식
    print(f'요청방식 : {request.method}')
    # print('요청방식 : {0}'.format(request.method))
    # if request.method == 'POST' :
    html = render_template('two.html')
    return html

@app.route('/three')
def three():
    html = render_template('three.html')
    return html

# @app.route('/<name>') #파라미터 넘기기 : 라우팅
# def index(name):
#     return render_template('index.html', name=name)

@app.route('/sleep')
def NoSleep():
    return "<h1>주무시지 마시오</h1>"