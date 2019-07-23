from flask import Flask

app = Flask(__name__)

@app.route('/')
def helloword():
    return "<h1>Hello World</h1>"

@app.route('/sleep')
def NoSleep():
    return "<h1>주무시지 마시오</h1>"


if __name__=="__main__":
    app.run()