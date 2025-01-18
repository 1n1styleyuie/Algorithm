# 2870 s4
import sys
input = sys.stdin.readline


n = int(input())
res = []
for _ in range(n):
    aa = input().rstrip()
    num = ''
    for a in aa:
        if a in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
            num += a
        else:
            if num:
                res.append(int(num))
                num = ''
    if num:
        res.append(int(num))

res.sort()
for r in res:
    print(r)