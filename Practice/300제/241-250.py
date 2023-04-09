#241
import datetime
now = datetime.datetime.now()
print(now)
print('\n')

#242
import datetime
now = datetime.datetime.now()
print(now,type(now))
print('\n')

#243
import datetime
today = datetime.date.today()
for i in range(5,0,-1) :
    diff_days = datetime.timedelta(days=i)
    print(today-diff_days)
print('\n')

#244
import datetime
now = datetime.datetime.now()
print(now.strftime('%X'))
print('\n')

#245
import datetime
day = "2020-05-04"
set = datetime.datetime.strptime(day, '%Y-%m-%d')
print(set,type(set))
print('\n')

#246

print('\n')

#247
import os
a = os.getcwd()
print(a, type(a))

#249
import os
os.rename("C:/Python/a.txt", "C:/Python/b.txt")

#250
import numpy
for i in numpy.arange(0, 5, 0.1):
    print(i)