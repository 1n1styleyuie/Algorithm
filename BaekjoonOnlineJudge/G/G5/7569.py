# 7569
import sys
from collections import deque

input = sys.stdin.readline

dx = [1, -1, 0, 0, 0, 0]
dy = [0, 0, 1, -1, 0, 0]
dz = [0, 0, 0, 0, 1, -1]


def bfs():
    while q:
        z, x, y = q.popleft()
        for i in range(6):
            nx, ny, nz = x + dx[i], y + dy[i], z + dz[i]
            if 0 <= nx < N and 0 <= ny < M and 0 <= nz < H:
                if arr[nz][nx][ny] == 0:
                    arr[nz][nx][ny] = arr[z][x][y] + 1
                    q.append((nz, nx, ny))


M, N, H = map(int, input().split())
arr = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]
q = deque()
for i in range(H):
    for j in range(N):
        for k in range(M):
            if arr[i][j][k] == 1:
                q.append((i, j, k))
bfs()

res = False
ans = 0
for i in range(H):
    for j in range(N):
        for k in range(M):
            if arr[i][j][k] == 0:
                res = True
            ans = max(ans, arr[i][j][k])

if res:
    print(-1)
else:
    print(ans - 1)