# 1308 s5
import sys
input = sys.stdin.readline
from datetime import date

y1, m1, d1 = map(int, input().split())
y2, m2, d2 = map(int, input().split())

if y2-y1 > 1000 or (y2-y1 == 1000 and m1 <= m2 and d1 <= d2):
    print('gg')
else:
    time1 = date(y1, m1, d1)
    time2 = date(y2, m2, d2)
    time = str(time2.toordinal() - time1.toordinal())    

    print(f'D-{time}')
