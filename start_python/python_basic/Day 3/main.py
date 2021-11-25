### Viết chương trình in ra thời gian đếm ngược đến XMas 2021 sau mỗi khoảng thời gian nhất định.
import time
from datetime import datetime

while True:
    time.sleep(10)
    XMAS_DATE = datetime(year=2021, month=12, day=24)
    countdown = XMAS_DATE - datetime.now()
    print(f"Countdown to Xmas 2021: {countdown}")
    if countdown == 0:
        break


### Viết chương trình trả ra từ điển với key là các số trong list, value là số lần xuất hiện của số trong list
from collections import Counter
my_list = [10, 21, 21, 40, 40, 52, 52, 1, 1, 2, 2, 2, 2, 11, 11, 11, 11, 25, 24, 24, 60, 40]
c = Counter(my_list)
print(c)

### Hãy viết chương trình in ra các hình sau (dùng ký tự '*' và ký tự space) với n là số dòng. Vd: n = 4:
#       *
#     * *
#   * * *
# * * * *

A=int(input('Enter a number: '))
#Hinh 1
print("Hinh 1")
for i in range (1,A+1):
    print('* '*i)

#Hinh 2
print("Hinh 2")
for i in range (1,A+1):
    print('* '*(A+1-i),'  '*(i-1))

#Hinh 3
print("Hinh 3")
for i in range (1,A+1):
    print('  '*(i-1),'* '*(A+1-i))

#Hinh 4
print("Hinh 4")
for i in range (1,A+1):
    print('  '*(A-i),'* '*i)

#Hinh 5
print("Hinh 5")
for i in range (1,A+1):
    print('  '*(A-i),'* '*(2*i-1),'  '*(A-i))

#Hinh 6
print('Hinh 6')
for i in range (1,A+1):
    print('* '*A)

#Hinh 7
print('Hinh 7')
for i in range(1,A+1):
    if i==1:
        print('* '*A)
    elif i in range(2,A):
        print('* ', '  ' * (A - 3), '*')
    else:
        print('* ' * A)