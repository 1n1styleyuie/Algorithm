# 1359
import sys
input = sys.stdin.readline
from itertools import combinations

n, m, k = map(int, input().split())
res = 0
arr = [i for i in range(n)]
comb = combinations(arr, m)
count = 0
for c in comb:
    cnt = 0
    count += 1
    for i in range(m):
        if c[i] < m:
            cnt += 1
    if cnt >= k:
        res += 1

print(res/count)