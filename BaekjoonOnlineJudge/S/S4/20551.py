# 20551 s4
import sys
input = sys.stdin.readline


n, m = map(int, input().split())
a = []
for _ in range(n):
    a.append(int(input()))

a.sort()

for _ in range(m):
    start, end = 0, n-1
    d = int(input())
    res = -1
    while start <= end:
        mid = (start + end) // 2
        if a[mid] == d:
            res = mid

        if a[mid] >= d:
            end = mid - 1
        else:
            start = mid + 1

    print(res)
