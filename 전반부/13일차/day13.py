from pymongo import MongoClient
import datetime

client = MongoClient('mongodb://127.0.0.1:27017/')
db = client.python_db

def insert():
    title = input('제목 : ')
    writer = input('작성자 : ')
    contents = input('내용 : ')

    db.blog.insert_one({
        'title': title,
        'contents': contents,
        'writer': writer,
        'wdate': datetime.datetime.now().strftime('%Y-%m-%d, %H:%M:%S')
    })
    print('-' * 50)

def select():
    rows = db.blog.find()
    for row in rows:
        print(row['title'], row['contents'], row['writer'], row['wdate'])
    print('-'*50)

def update():
    from_title = input('원본제목 : ')
    to_title = input('수정제목 : ')

    db.blog.update_one({'title': from_title},{'$set':{'title':to_title}})
    print('-' * 50)

def delete():
    title = input('삭제제목 :')

    db.blog.delete_one({'title': title})
    print('-' * 50)

while 1:
    sel = input('1.목록 2.추가 3.수정 4.삭제 0.종료')
    if sel == '1':
        select()
    elif sel == '2':
        insert()
    elif sel == '3':
        update()
    elif sel == '4':
        delete()
    elif sel == '0':
        break
