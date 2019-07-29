from flask import Flask, render_template, request, redirect, session, url_for
import datetime

app = Flask(__name__, template_folder='templates/inh')
app.secret_key = 'soijowijfwpojfwoe' #세션 변조 여부 체크

@app.route('/')
@app.route('/index')
def index():
    print(datetime.datetime.now())
    if not session.get('logged_in'):
        return render_template('index_css.html')
    else:
        if request.method == 'POST':
            # username = getname(request.form['username'])
            # return render_template('index.html', data=getfollowedby(username))
            username = request.form['username']
            return render_template('index_css.html', data=username)
        return render_template('index_css.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
	if request.method == 'GET':
		return render_template('login.html')
	else:
		name = request.form['username'] #입력한 값받기
		passw = request.form['password']
		try:
			#DB에서 회원정보 조회
			session['logged_in'] = True
			session['user_id'] = name
			return redirect(url_for('index'))
		except:
			return "Dont Login"


@app.route('/register/', methods=['GET', 'POST'])
def register():
	if request.method == 'POST':
		username=request.form['username']
		password=request.form['password']

		#DB에 회원정보 등록
		return render_template('login.html')
	return render_template('register.html')


@app.route('/logout')
def logout():
	if session.get('logged_in'):
		del session['logged_in']
	if session.get('user_id'):
		del session['user_id']

	session.pop('logged_in', None)
	session.pop('user_id', None)
	return redirect(url_for('index'))

@app.route('/about')
def about():
    return render_template('about.html', title='About')

