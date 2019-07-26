from flask import Flask, render_template, request, current_app
import os
from werkzeug.utils import secure_filename
from flask import send_from_directory, send_file
from flask import flash

#파일 업로드 폴더 지정하기
UPLOAD_FOLDER = 'uploads' #절대경로로 준다.
#업로드 허용 가능한 파일 확장자
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif', 'csv'])

#플라스크 객체 만들기
app = Flask(__name__)
app.secret_key = "asdawqewq232432sfdsf"

#설정파일에 저장하기
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
#업로드 용량 제한
app.config['MAX_CONTENT_LENGTH'] = 20 * 1024 * 1024*100 #업로드 최대크기-20M


#파일 업로드 html 랜더링
@app.route("/")
def index():
    return render_template("upload.html")


#파일 확장자 사용 가능 여부 
def allowed_file(filename):
    print(filename)
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# s = 'one:two:three:four'
# s.split(':', 2)
# ['one', 'two', 'three:four']
# s.rsplit(':', 1)
# ['one:two:three', 'four']


#파일 전송하기 
@app.route("/file/save",  methods=['post'])
def file_upload():
    file = request.files['upload']  #files로 받아야 한다. get- args, post - form, file - files로 받는다.

    if file.filename == '':
        flash('No selected file')
        return "file 을 선택하지 않았습니다"
    
    #파일을 선택했고, 확장자가 업로드를 허용한다면
    if file and allowed_file(file.filename):
        #filename = secure_filename(file.filename)
        filename = file.filename
        sfilename = os.path.join(current_app.root_path, app.config['UPLOAD_FOLDER'], filename)

        app.logger.debug(sfilename)
        
        file.save(sfilename)
        return filename+" 업로드 성공"
    else:
        print(file.filename)

        
@app.route('/download/<filename>')
def download(filename):
    uploads = os.path.join(current_app.root_path, app.config['UPLOAD_FOLDER'])
    app.logger.debug(filename)
    return send_from_directory(directory=uploads, filename=filename)

    '''
    sfilename = os.path.join(uploads, filename)
    ext = '.' in filename and filename.rsplit('.', 1)[1].lower()
    file_mimeType = 'image/jpeg'
    if ext in ('pdf'):
        file_mimeType = 'application/pdf'
    elif ext in ('csv'):
        file_mimeType = 'text/csv'
    elif ext in ('txt'):
        file_mimeType = 'text/plain'

    return send_file(sfilename,
                     mimetype=file_mimeType,
                     attachment_filename=filename,  # 다운받아지는 파일 이름.
                     as_attachment=True)
    '''


if __name__ == "__main__":
    app.debug = True  #서버 자동 재시작
    app.run(host='127.0.0.1', port=8000)