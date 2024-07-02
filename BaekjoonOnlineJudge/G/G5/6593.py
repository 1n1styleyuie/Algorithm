import sys
from collections import deque
input = sys.stdin.readline

dx = [1, -1, 0, 0, 0, 0]
dy = [0, 0, 1, -1, 0, 0]
dz = [0, 0, 0, 0, 1, -1]


def bfs(i, j, k):
    q = deque()
    q.append((i, j, k))
    visited[i][j][k] = 1
    while q:
        x, y, z = q.popleft()
        for i in range(6):
            nx, ny, nz = x + dx[i], y + dy[i], z + dz[i]
            if 0<=nx<L and 0<=ny<R and 0<=nz<C:
                if building[nx][ny][nz] == 'E':
                    print(f'Escaped in {visited[x][y][z]} minute(s).')
                    return
                if building[nx][ny][nz] == '.' and visited[nx][ny][nz] == 0:

                    visited[nx][ny][nz] = visited[x][y][z] + 1
                    q.append((nx, ny, nz))
    print('Trapped!')


while True:
    L, R, C = map(int, input().split())

    if L == 0 and R == 0 and C == 0:
        break

    building = []
    for _ in range(L):
        building.append([list(map(str, input().strip())) for _ in range(R)])
        input()

    visited = [[[0 for _ in range(C)] for _ in range(R)] for _ in range(L)]

    for i in range(L):
        for j in range(R):
            for k in range(C):
                if building[i][j][k] == 'S':
                    bfs(i, j, k)
