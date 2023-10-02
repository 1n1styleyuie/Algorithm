import sys
input = sys.stdin.readline
from collections import deque


# 7576
delta = [[0, 1], [0, -1], [1, 0], [-1, 0]]
m, n = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
q = deque()
for i in range(n):
    for j in range(m):
        if arr[i][j] == 1:
            q.append((i, j))
while q:
    i, j = q.popleft()
    for di, dj in delta:
       ni, nj = i+di, j+dj
       if 0<=ni<n and 0<=nj<m:
           if arr[ni][nj] == -1:
               continue
           if arr[ni][nj] == 0:
               arr[ni][nj] = arr[i][j] + 1
               q.append((ni, nj))




flg = False
for i in range(n):
    for j in range(m):
        if arr[i][j] == 0:
            flg = True
            break

if flg:
    print(-1)
else:
    print(max(map(max, arr))-1)