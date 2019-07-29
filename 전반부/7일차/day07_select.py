import sqlite3

conn  = sqlite3.connect('database_new.db')

c = conn.cursor()
c.execute('SELECT * FROM users')

print('One -> \n', c.fetchone())

print('Three -> \n', c.fetchmany(size = 3))

print('All -> \n', c.fetchall())

print()

for row in c.fetchall():
    print('retrieve2 > ', row) #조회  x


for row in c.execute('SELECT * FROM users ORDER BY id DESC'):
    print('retrieve3 > ', row)

param1 = (12,)
c.execute('SELECT * FROM users WHERE id =?', param1)
print('param1',c.fetchone())
print('param1',c.fetchall())

param2 = 13
c.execute("SELECT * FROM users WHERE id='%s'"% param2)
print('param2',c.fetchone())
print('param2',c.fetchall())


c.execute("SELECT * FROM users WHERE id= :Id", {"Id": 19}) # 딕셔너리로 주기
print('param3',c.fetchone())
print('param3',c.fetchall())

param4 = (12,14)
c.execute("SELECT * FROM users WHERE id IN(?,?)", param4)
print('param4',c.fetchone())
print('param4',c.fetchall())

with conn:
    # Dump 출력(데이터베이스 백업 시 중요)
    # SQL 텍스트 형식으로 데이터베이스를 덤프
    with open('dump.sql', 'w') as f:
        for line in conn.iterdump():
            f.write('%s\n' % line)
        print('Dump Print Complete.')

# UPDATE 테이블명 SET 컬럼명=새 값 where