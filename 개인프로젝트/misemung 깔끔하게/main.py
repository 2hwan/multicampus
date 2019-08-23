from flask import Flask, render_template, request, session
import json
from urllib.request import urlopen
from urllib.parse import quote
import re
import pandas as pd
import folium

import database as db

app = Flask(__name__, template_folder='view')
app.secret_key='GDFGDFGDFGD'

@app.route('/')
def index() :
    html = render_template('index.html')
    return html


@app.route('/now', methods=['GET', 'POST'])
def now() :
    url_base = 'http://openapi.airkorea.or.kr/openapi/services/rest/ArpltnInforInqireSvc/getCtprvnMesureSidoLIst'
    service_key = '?ServiceKey=6tVQ7lv4nGhr5qdk2VmHwzbu%2B%2Bewy6eYJjVDwqBVNpmcr%2BaYoTHb4cxtX%2F0kMfzwDj9EIe7cER7BNN3BlRM9Ow%3D%3D'
    page = '&numOfRows=10&pageNo=1'
    sidoname = '&sidoName=' + quote('인천')
    daily = '&searchCondition=DAILY'
    url = url_base + service_key + page + sidoname + daily

    xml = urlopen(url)

    data = xml.read().decode('utf8')
    goo = re.findall('<cityName>.+</cityName>', data)
    list_a = []
    for line in goo:
        line = line.replace('<cityName>', '')
        line = line.replace('</cityName>', '')
        list_a.append(line)

    pm10 = re.findall('<pm10Value>.+</pm10Value>', data)
    list_b = []
    for line in pm10:
        line = line.replace('<pm10Value>', '')
        line = line.replace('</pm10Value>', '')
        list_b.append(line)

    pm25 = re.findall('<pm25Value>.+</pm25Value>', data)
    list_c = []
    for line in pm25:
        line = line.replace('<pm25Value>', '')
        line = line.replace('</pm25Value>', '')
        list_c.append(line)

    so2 = re.findall('<so2Value>.+</so2Value>', data)

    list_d = []
    for line in so2:
        line = line.replace('<so2Value>', '')
        line = line.replace('</so2Value>', '')
        list_d.append(line)

    co = re.findall('<coValue>.+</coValue>', data)

    list_e = []
    for line in co:
        line = line.replace('<coValue>', '')
        line = line.replace('</coValue>', '')
        list_e.append(line)

    o3 = re.findall('<o3Value>.+</o3Value>', data)

    list_f = []
    for line in o3:
        line = line.replace('<o3Value>', '')
        line = line.replace('</o3Value>', '')
        list_f.append(line)

    no2 = re.findall('<no2Value>.+</no2Value>', data)

    list_g = []
    for line in no2:
        line = line.replace('<no2Value>', '')
        line = line.replace('</no2Value>', '')
        list_g.append(line)

    dtime = re.findall('<dataTime>.+</dataTime>', data)

    list_h = []
    for line in dtime:
        line = line.replace('<dataTime>', '')
        line = line.replace('</dataTime>', '')
        list_h.append(line)

    dataset = {'구': list_a, 'pm10': list_b, 'pm25': list_c, 'so2': list_d, 'co': list_e, 'o3': list_f, 'no2': list_g,
               'dateTime': list_h}
    df = pd.DataFrame(dataset)
    df.drop(0, inplace=True)
    df.drop(9, inplace=True)
    df.set_index('구', inplace=True)
    print(df)

    for i in range(0, 8):
        for j in range(0, 6):
            if df.iloc[i][j] == '-':
                df.iloc[i][j] = 0

    db.add_air(df)
    df.to_csv("static/dust.csv", encoding='utf-8', sep=',')
    dff = pd.read_csv('static/dust.csv', thousands=',', encoding='utf-8')
    dff.set_index('구', inplace=True)

    geo_path = 'static/skorea-municipalities-2018-geo.json'
    geo_json = json.load(open(geo_path, encoding='utf-8'))
    map = folium.Map(location=[37.454441, 126.708096],
                     zoom_start=11, tiles='Mapbox Control Room')

    map.choropleth(geo_data=geo_json,
                   data=dff['pm10'],
                   columns=[dff.index, dff['pm10']],
                   fill_color='PuBu',
                   key_on='feature.properties.name',
                   fill_opacity=1,
                   line_opacity=1,
                   highlight=True)

    map.save('view/dust.html')

    html = render_template('dust.html')
    return html

@app.route('/hour', methods=['GET', 'POST'])
def hour() :
    html = render_template('hour.html')
    return html

@app.route('/future', methods=['GET', 'POST'])
def future() :
    html = render_template('future.html')
    return html

@app.route('/sample', methods=['GET', 'POST'])
def sample() :
    html = render_template('dust.html')
    return html


@app.route('/login', methods=['get','post'])
def login() :

    html = render_template('login.html')
    return html

@app.route('/login_pro', methods=['get','post'])
def login_pro() :
    id = request.form['id']
    pwd = request.form['pwd']
    session['m_session'] = db.login(id,pwd)

    html = render_template('login_pro.html')
    return html

@app.route('/register', methods=['GET', 'POST'])
def register():
    html = render_template('register.html')
    return html

@app.route('/register_pro', methods=['GET', 'POST'])
def register_pro():
    # 파라미터 추출
    id = request.form['id']
    pwd = request.form['pwd']
    # 점수 정보 저장
    db.register(id,pwd)

    html = render_template('register_pro.html')
    return html

@app.route('/logout', methods=['get','post'])
def logout() :

    session['m_session'] = False

    html = render_template('index.html')
    return html


app.run(host='127.0.0.1', port=8080)