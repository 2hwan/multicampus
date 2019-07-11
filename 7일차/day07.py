import time
from datetime import datetime, timedelta

timestamp_now = time.time() # 절대 시간
print(timestamp_now)

datetime_now = datetime.now() # 익숙한시간
print(datetime_now)

delta_datetime = timedelta(days = -30)
print(datetime_now + delta_datetime)

end_datetime = datetime_now + delta_datetime
print(end_datetime.timetuple())
end_timestamp = time.mktime(end_datetime.timetuple()) #datetime -> timestamp로

print(timestamp_now)
print(datetime.fromtimestamp(timestamp_now)) # timestamp -> 를 datetime 형식으로
print(end_timestamp)

import  calendar

print(calendar.calendar(2019))

year2019 = calendar.calendar(2019)
print(type(year2019))

print(calendar.prmonth(2019,7))
print(calendar.prmonth(datetime_now.year,datetime_now.month))

print('\n\n오늘 요일 인덱스:\n\n')
print(calendar.weekday(2019,7,11))
weekDay = ['월','화','수','목','금','토','일']
print('오늘은 {} 입니다'.format(weekDay[calendar.weekday(2019,7,11)]))

print('크리스마스 {} 입니다'.format(weekDay[calendar.weekday(2019,12,25)]))