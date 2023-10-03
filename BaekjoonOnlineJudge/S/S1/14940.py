# 14940
import sys
input = sys.stdin.readline
from collections import deque

delta = [[1, 0], [-1, 0], [0, 1], [0, -1]]

def bfs(i, j):
    q = deque()
    q.append((i, j))
    while q:
        x, y = q.popleft()
        for dx, dy in delta:
            nx, ny = x+dx, y+dy
            if 0<=nx<N and 0<=ny<M and arr[nx][ny] == 1:
                if not visited[nx][ny]:
                    visited[nx][ny] = visited[x][y] + 1
                    q.append((nx, ny))


N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
visited = [[0]*M for _ in range(N)]
for i in range(N):
    for j in range(M):
        if arr[i][j] == 2:
            bfs(i, j)

for i in range(N):
    for j in range(M):
        if arr[i][j] == 1 and visited[i][j] == 0:
            visited[i][j] = -1

for i in range(N):
    print(*visited[i])