import sqlite3

print('sqlite3.version',sqlite3.version)
print('sqlite3.sqlite_version', sqlite3.sqlite_version)

# DB 생성 & Autocommit
# 본인 DB 파일 경로
conn  = sqlite3.connect('database_new.db')

# DB생성(메모리)
# conn = sqlite3.connect(':memory:')

# Cursor 연결
c = conn.cursor()
print('Cursor Type : ', type(c))

# 테이블 생성(Datatype : TEXT NUMERIC INTEGER REAL BLOB)
c.execute(
    '''CREATE TABLE IF NOT EXISTS users
        (id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT,
        email TEXT,
        phone TEXT,
        website TEXT,
        regdate TEXT)
    ''') # id INTEGER PRIMARY KEY AUTOINCREMENT, 안겹치게 자동증가 시킴, 대소문자 구분 x

import datetime
#삽입 날짜 생성
now = datetime.datetime.now()
print('now', now)

nowDatetime = now.strftime('%Y-%m-%D %H:%M:%S')
print('nowDatetime', nowDatetime)

sql = '''INSERT INTO users (username, email, phone, website, regdate) VALUES ('Kim', 'Kim@naver.com', '010-0000-0000', 'Kim.com', ?)'''

#데이터 삽입
c.execute(sql, (nowDatetime,))

sql1 = """ INSERT INTO users
(username, email, phone, website, regdate)
VALUES (?, ?, ?, ?, ?)"""

c.execute(sql1, ('Park', 'Park@naver.com',
                '010-1111-1111', 'Park.com',
                 nowDatetime))

# c.execute('''DELETE FROM users WHERE id=6''')
# c.execute('''DELETE FROM users WHERE id=7''')
# c.execute('''DELETE FROM users WHERE id=8''')
# c.execute('''DELETE FROM users WHERE id=9''')
# c.execute('''DELETE FROM users WHERE id=10''')
#

#Many 삽입(튜플, 리스트)
userList = (
     ('Lee', 'Lee@naver.com', '010-2222-2222', 'Lee.com', nowDatetime),
     ('Cho', 'Cho@naver.com', '010-3333-3333', 'Cho.com', nowDatetime),
     ('Yoo', 'Yoo@naver.com', '010-4444-4444', 'Yoo.com', nowDatetime)
)
c.executemany("INSERT INTO users(username, email, phone, website, regdate) VALUES (?, ?, ?, ?, ?)", userList)



conn.commit()

# c.execute('''INSERT INTO users
#     (id, username, email, phone, website, regdate) VALUES (?, ?, ? ,? ,? ,?),
#         (2, 'Park', 'Park@naver.com', '010-1111-1111', 'Park.com', nowDatetime)
#     ''')
conn.close()