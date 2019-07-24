import json
from flask import Flask

app = Flask(__name__, template_folder='view')

@app.route('/')
def index() :

    test_dic = {
        'a1' : 100,
        'a2' : '문자열'
    }

    #JSON Encoding : Python Object (Dictionary, List, Tuple 등)를 JSON 문자열로 변경
    json_data = json.dumps(test_dic, indent=4, ensure_ascii=False)
    # indent 는 들여쓰기, ensure_ascii 는 한글 처리
    print(type(json_data), json_data)

    #JSON Decoding  : JSON 문자열을 Python Object (Dictionary, List, Tuple 등)로 변경
    python_data = json.loads(json_data)
    print(type(python_data), python_data)

    return json_data
    
app.run(host='127.0.0.1', port=80)

