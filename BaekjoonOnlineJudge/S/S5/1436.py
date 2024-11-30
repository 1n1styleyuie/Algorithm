# 1436 s5
import sys
input = sys.stdin.readline

n = int(input())
num = 666
cnt = 0

# 계속 숫자를 늘려가면서 탐색하면 된다.
while True:
    if '666' in str(num):
        cnt += 1
    
    if cnt == n:
        print(num)
        break

    num += 1