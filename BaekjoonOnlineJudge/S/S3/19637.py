# 19637 s3
import sys
input = sys.stdin.readline


n, m = map(int, input().split())
g = []
power = []
for _ in range(n):
    a, b = input().split()
    g.append(a)
    power.append(int(b))


for _ in range(m):
    num = int(input())
    start = 0
    end = n-1
    res = 0
    while start <= end:
        mid = (start + end) // 2
        if power[mid] >= num:
            res = mid
            end = mid - 1
        else:
            start = mid + 1

    print(g[res])