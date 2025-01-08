# 2422 s4
import sys
input = sys.stdin.readline


n, m = map(int, input().split())
arr = [[0] * n for _ in range(n)]

for _ in range(m):
    a, b = map(int, input().split())
    arr[a-1][b-1] = 1
    arr[b-1][a-1] = 1


cnt = 0
for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            if not arr[i][j] and not arr[i][k] and not arr[j][k]:
                cnt += 1

print(cnt)