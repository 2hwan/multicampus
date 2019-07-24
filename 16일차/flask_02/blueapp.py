from day16_flask.main import app

if __name__=="__main__":
    app.run(host='127.0.0.1', port = 80, debug=True) #모든 클라이언트에 접속허용 0.0.0.0
    #127.0.0.1 로 들어가야함
    #허용하지면 원격은 허용안함 0.0.0.1
    # app.run()
