# 32185 s5
import sys
input = sys.stdin.readline


n, m = map(int, input().split())
v, p, s = map(int, input().split())
arr = []
for i in range(1, n+1):
    vi, pi, si = map(int, input().split())
    if v + p + s >= vi + pi + si:
        arr.append((vi+pi+si, i))

arr.sort(reverse=True, key=lambda x : x[0])

res = [0]
for t, idx in arr[:m-1]:
    res.append(idx)

print(*res)