# 1059 s4
import sys
input = sys.stdin.readline

l = int(input())
s = list(map(int, input().split()))
n = int(input())

s.sort()

if n in s:
    print(0)
else:
    max_num = 1001
    min_num = 0
    for i in range(l):
        if s[i] > n:
            max_num = s[i]
            break
        if s[i] < n:
            min_num = s[i]

    cnt = (n - min_num) * (max_num - n) - 1
    print(cnt)
