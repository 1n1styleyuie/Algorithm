# 14716 s1
import sys
input = sys.stdin.readline
from collections import deque


delta = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]
def bfs(x, y):
    q = deque()
    q.append((x, y))
    visited[x][y] = 1
    while q:
        i, j = q.popleft()
        for di, dj in delta:
            ni, nj = i+di, j+dj
            if 0 <= ni < m and 0 <= nj < n:
                if arr[ni][nj] == 1 and not visited[ni][nj]:
                    visited[ni][nj] = 1
                    q.append((ni, nj))


m, n = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(m)]
visited = [[0] * n for _ in range(m)]
res = 0

for i in range(m):
    for j in range(n):
        if arr[i][j] == 1 and not visited[i][j]:
            bfs(i, j)
            res += 1

print(res)