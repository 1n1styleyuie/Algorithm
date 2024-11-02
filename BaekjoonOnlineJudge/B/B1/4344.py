# 4344 b1
import sys
input = sys.stdin.readline

c = int(input())

for _ in range(c):
    n = list(map(int, input().split()))
    avg = sum(n[1:])/n[0]

    cnt = 0
    for i in n[1:]:
        if i > avg:
            cnt += 1
    
    percent = (cnt/n[0])*100
    print('%.3f' %percent + '%')