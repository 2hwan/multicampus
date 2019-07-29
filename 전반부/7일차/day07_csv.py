# 파이썬 excel, csv 읽기

import csv

with open('./csv/data/data1.csv', 'r') as f :
    reader = csv.reader(f)
    next(reader) #헤더를 스킵한다

    print(reader)
    print(type(reader))
    print(dir(reader))
    print()

    for c in reader :
        print(c)

# 예제 2
with open('./csv/data/data2.csv', 'r') as f :
    reader = csv.reader(f, delimiter='|') #구분자 선택한다 default : ,
    next(reader) #헤더를 스킵한다

    print(reader)
    print(type(reader))
    print(dir(reader))
    print()

    for c in reader :
        print(c)



# 예제 3 (Dict 변환)
with open('./csv/data/data1.csv', 'r') as f :
    reader = csv.DictReader(f) #구분자 선택한다 default : ,
    next(reader) #헤더를 스킵한다

    print(reader)
    print(type(reader))
    print(dir(reader))
    print()

    for c in reader :
        for k, v in c.items():
            print(k, v)
        print('-------')


# 예제 4
# 리스트 데이터를 csv 파일에 저장
w = [[1, 2 ,3],
     [4, 5 ,6],
     [7, 8, 9],
     [10, 11, 12],
     [13, 14, 15]]

with open('./csv/data/out_data1.csv', 'w') as f :
    wt = csv.writer(f)

    print(dir(wt))
    print(type(wt))
    for v in w:
        wt.writerow(v)

with open('./csv/data/out_data2.csv', 'w', newline = '') as f : #default \n 이므로
    wt = csv.writer(f)
    wt.writerows(w)