# 2178
import sys
input = sys.stdin.readline
from collections import deque

delta = [[1, 0], [-1, 0], [0, 1], [0, -1]]

def bfs(i, j):
    q = deque()
    visited = [[0]*M for _ in range(N)]
    q.append((i, j))
    visited[i][j] = 1
    while q:
        x, y = q.popleft()
        for dx, dy in delta:
            nx, ny = x+dx, y+dy
            if 0<=nx<N and 0<=ny<M and visited[nx][ny] == 0 and arr[nx][ny] == 1:
                q.append((nx, ny))
                visited[nx][ny] = visited[x][y] + 1
    return visited[N-1][M-1]


N, M = map(int, input().split())
arr = [list(map(int, input().rstrip())) for _ in range(N)]
print(bfs(0, 0))