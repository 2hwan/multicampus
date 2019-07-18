import pymysql

conn = pymysql.connect(host = 'localhost',
                       port = 3306,
                       user = 'root',
                       passwd = '1234',
                       db = 'pyMysql_db',
                       charset = 'utf8')
curs = conn.cursor() # 튜플커서

while 1 :
    sel = input('1.목록 2.추가 3.수정 4.삭제 0.종료')
    if sel == '1':
        sql = 'select * from member'
        curs.execute(sql)
        rows = curs.fetchall()
        for row in rows:
            print(row[0], row[1], row[2], row[3])
        print('-'*50)
    elif sel == '2':
        sql = 'insert into member(userid, pwd, name, email, regdate) values(%s, %s, %s, %s, now())'
        userid = input('id :')
        name = input('name :')
        email = input('email :')

        curs.execute(sql, (userid, '1234', name, email))
        conn.commit()
    elif sel == '3':
        sql = 'update member set email = %s where userid = %s'
        userid = input('id :')
        email = input('email :')

        curs.execute(sql, (email, userid))
        conn.commit()
        print('-' * 50)
    elif sel == '4':
        sql = 'delete from memeber where userid = %s'
        userid = input('id :')

        curs.execute(sql, userid)
        conn.commit()
        print('-' * 50)
    elif sel == '0':
        conn.close()
        break
