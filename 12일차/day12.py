import pymysql

conn = pymysql.connect(host = 'localhost',
                       port = 3306,
                       user = 'root',
                       passwd = '1234',
                       db = 'pyMysql_db',
                       charset = 'utf8')
curs = conn.cursor() # 튜플커서
sql = 'select * from member'
curs.execute(sql)

rows = curs.fetchall()
print(rows)
print(rows[0])

for row in rows:
    print(row)
print('-' *50)

rows = curs.fetchall()
print(rows) #커서가 내려감

curs.execute(sql)
row = curs.fetchone()
print(row)

curs.execute(sql)
row = curs.fetchmany(3)
print(row)

curs = conn.cursor(pymysql.cursors.DictCursor)
curs.execute(sql)
rows = curs.fetchall()
for row in rows:
    print(type(row), row['userid'], row['name'], row['pwd'])


conn.close()