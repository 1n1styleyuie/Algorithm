#16439 s4
import sys
input = sys.stdin.readline
from itertools import combinations


n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

res = 0
for comb in combinations(range(m), 3):
    total = 0
    for i in range(n):
        total += max(arr[i][comb[0]], arr[i][comb[1]], arr[i][comb[2]])
    res = max(res, total)

print(res)