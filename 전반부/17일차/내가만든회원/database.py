import pymysql

# 데이터 베이스에 접속하는 함수
def get_connection() :
    conn = pymysql.connect(host='127.0.0.1', user='root',
            password='1234', db='pymysql_db'
            , charset='utf8')

    return conn

# 학생 목록을 가져오는 함수
def get_student_list(stu_name) :
    # 데이터베이스 접속
    conn = get_connection()
    # 쿼리문
    sql = '''select stu_idx, stu_name, stu_age, stu_addr
             from student_table'''

    if stu_name != None and len(stu_name) > 0 :     # 검색어가 있을 경우
        sql += ' where stu_name like %s'

    sql += ' order by stu_idx desc'

    # 쿼리문 실행
    cursor = conn.cursor(pymysql.cursors.DictCursor)

    if stu_name != None and len(stu_name) > 0 :
        cursor.execute(sql, (f'%{stu_name}%')) #검색조건
    else :
        cursor.execute(sql)

    # 결과를 가져온다.
    result = cursor.fetchall()
    # 데이터를 추출한다.
    # temp_list = []
    # for row in result :
    #     temp_dic = {}
    #     temp_dic['stu_idx'] = row[0]
    #     temp_dic['stu_name'] = row[1]
    #     temp_dic['stu_age'] = row[2]
    #     temp_dic['stu_addr'] = row[3]
    #
    #     temp_list.append(temp_dic)

    conn.close()
    return result

# 학생 정보를 저장한다.
def add_student(stu_name, stu_age, stu_addr) :
    # 쿼리문
    sql = '''insert into student_table
             (stu_name, stu_age, stu_addr)
             values (%s, %s, %s)'''
    # 데이터 베이스 접속
    conn = get_connection()

    # 쿼리 실행
    # cursor = conn.cursor() #튜플 커서
    cursor = conn.cursor() #딕셔너리 커서

    cursor.execute(sql, (stu_name, stu_age, stu_addr))
    conn.commit()

    # 방금 저장한 학생의 번호를 가져온다.
    sql2 = 'select max(stu_idx) from student_table'
    cursor.execute(sql2)
    result = cursor.fetchone()
    idx = result[0]

    # 접속 종료
    conn.close()

    return idx

# 학생 한명의 정보를 가져오는 함수
def get_student_info(stu_idx) :
    # 쿼리문
    sql = '''select stu_idx, stu_name, stu_age, stu_addr
             from student_table
             where stu_idx = %s'''  #mysql이면 다 %s
    # 접속
    conn = get_connection()
    # 쿼리 실행
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    cursor.execute(sql, (stu_idx))

    result = cursor.fetchone()
    #데이터 추출


    conn.close()
    return result
    # return result
# 점수 정보를 저장한다.
def add_point(point_stu_idx, point_stu_grade, point_stu_kor) :
    # 쿼리문
    sql = '''insert into point_table
             (point_stu_idx, point_stu_grade, point_stu_kor)
             values (%s, %s, %s)'''
    # 데이터베이스 접속
    conn = get_connection()
    # 쿼리 실행
    cursor = conn.cursor()
    cursor.execute(sql, (point_stu_idx, point_stu_grade, point_stu_kor))
    conn.commit()

    conn.close()

# 학생 점수 가져오기
def get_point(stu_idx) :
    # 쿼리문
    sql = '''select point_stu_grade, point_stu_kor
             from point_table
             where point_stu_idx=%s
             order by point_stu_grade'''
    # 접속
    conn = get_connection()
    # 쿼리 실행
    cursor = conn.cursor()
    cursor.execute(sql, (stu_idx))
    result = cursor.fetchall()
    # 데이터 추출
    result_list = []

    for result_dic in result :
        temp_dic = {}
        temp_dic['point_stu_grade'] = result_dic[0]
        temp_dic['point_stu_kor'] = result_dic[1]

        result_list.append(temp_dic)

    conn.close()

    return result_list

# 회원가입
def register(id,pwd) :
    # 쿼리문
    sql = '''insert into member
             (id, pwd)
             values (%s, %s)'''
    # 데이터 베이스 접속
    conn = get_connection()

    # 쿼리 실행
    cursor = conn.cursor()

    cursor.execute(sql, (id, pwd,))
    conn.commit()

    # 접속 종료
    conn.close()

def login(id,pwd) :
    conn = get_connection()
    sql = '''select id, pwd from member'''

    if id != None and len(id) > 0 :     # 검색어가 있을 경우
        sql += ' where id like %s'

    # 쿼리문 실행
    cursor = conn.cursor()

    if id != None and len(id) > 0 :
        cursor.execute(sql, (f'%{id}%')) #검색조건
    else :
        cursor.execute(sql)

    # 결과를 가져온다.
    result = cursor.fetchone()
    if pwd == result[1]:
        result = True
    else :
        result = False

    conn.close()
    return result


