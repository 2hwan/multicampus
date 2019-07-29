import csv

with open('./csv/data/population.csv', 'r') as f :
    reader = csv.reader(f)
    next(reader) #헤더를 스킵한다
    max = 0
    idx = ''
    for c in reader :
        mstr = c[1]
        mstr = mstr.replace(',','')

        c[1] = mstr
        print(c)
        if max < int(c[1]) :
            max = int(c[1])
            idx = c[0]

    print(idx,max)

with open('./csv/data/population.csv', 'r') as f :
    reader = csv.reader(f)
    #next(reader) #헤더를 스킵한다
    resultList = []
    for c in reader :
        #print(c)
        resultList.append(c)
resultList = resultList[1:]

for i in range(0, len(resultList)):
    data = resultList[i][1]
    data = int(data.replace(',',''))
    resultList[i][1] = data
print(resultList)

status = resultList[0][0]
max = resultList[0][1]
for i in range(0, len(resultList)):
    if max < resultList[i][1]:
        max = resultList[i][1]
        status = resultList[i][0]
print(status)

#XSL, XLSX
#pip install pandas
#pip install xlrd
#pip install openpyxl