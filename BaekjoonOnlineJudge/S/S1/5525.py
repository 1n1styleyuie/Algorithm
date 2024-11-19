# 5525 s1
import sys
input = sys.stdin.readline


n = int(input())
m = int(input())
s = input().rstrip()

res, idx, cnt = 0, 0, 0

while idx < (m-1):
    # IOI일 경우 카운트하고 인덱스를 인덱스+2 를 하여 위치를 바꿈
    # 카운트가 n과 같을 경우 res + 1 하고 카운트를 하나 줄여서 다음에 연속될 경우를 생각
    if s[idx:idx+3] == 'IOI':
        idx += 2
        cnt += 1
        if cnt == n:
            res += 1
            cnt -= 1
    else:
        idx += 1
        cnt = 0

print(res)