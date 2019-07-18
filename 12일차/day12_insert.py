import pymysql

conn = pymysql.connect(host = 'localhost',
                       port = 3306,
                       user = 'root',
                       passwd = '1234',
                       db = 'pyMysql_db',
                       charset = 'utf8')
curs = conn.cursor() # 튜플커서

sql = 'insert into member(userid, pwd, name, email, regdate) values(%s, %s, %s, %s, now())'

curs.execute(sql, ('ccc','1234','토이','toystory'))



data = (
    ('ddd','1234','알라딘','asdfasf@ala.co.kr'),
    ('EEE', '1234', '기생충', 'asdfasf@ala.co.kr'),
    ('fff', '1234', '인어공주', 'asdfasf@ala.co.kr')
)
curs.executemany(sql, data)

sql = 'update member set email = %s where userid = %s'
curs.execute(sql, ('aaa@aaaa.co.kr','aaa'))

sql = 'delete from member where userid = %s'
curs.execute(sql,('fff'))
conn.commit()


sql = 'select * from member'
curs.execute(sql)
rows = curs.fetchall()
print(rows)

conn.close()