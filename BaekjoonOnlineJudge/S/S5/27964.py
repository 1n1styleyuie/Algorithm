# 27964 s5
import sys
input = sys.stdin.readline


n = int(input())
arr = list(input().rstrip().split())
res = set()
for a in arr:
    if a[-6:] == 'Cheese' and a not in res:
        res.add(a)

if len(res) >= 4:
    print('yummy')
else:
    print('sad')