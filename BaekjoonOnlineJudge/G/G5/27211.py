# 27211 g5
import sys
input = sys.stdin.readline
from collections import deque


delta = [[0, 1], [0, -1], [1, 0], [-1, 0]]
def bfs(x, y):
    q = deque()
    q.append((x, y))
    visited[x][y] = 1
    while q:
        i, j = q.popleft()
        for di, dj in delta:
            ni, nj = i+di, j+dj
            if ni == n:
                ni = 0
            elif ni == -1:
                ni = n - 1

            if nj == m:
                nj = 0
            elif nj == -1:
                nj = m-1

            if 0 <= ni < n and 0 <= nj < m:
                if not visited[ni][nj] and arr[ni][nj] == 0:
                    q.append((ni, nj))
                    visited[ni][nj] = 1



n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
visited = [[0] * m for _ in range(n)]

res = 0
for x in range(n):
    for y in range(m):
        if not visited[x][y] and arr[x][y] == 0:
            bfs(x, y)
            res += 1

print(res)