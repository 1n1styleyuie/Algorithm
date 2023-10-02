from collections import deque

delta = [[0, 1], [0, -1], [1, 0], [-1, 0]]  # 델타함수


def bfs(n, m):
    q = deque()
    visited = [[-1] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 'W':
                q.append((i, j))
                visited[i][j] = 0

    while q:
        x, y = q.popleft()
        for di, dj in delta:
            ni, nj = x + di, y + dj
            # bfs탐색
            if 0 <= ni < n and 0 <= nj < m and arr[ni][nj] == 'L' and visited[ni][nj] == -1:
                visited[ni][nj] = visited[x][y] + 1
                q.append((ni, nj))

    res = 0
    for i in range(n):
        res += sum(visited[i])
    return res


T = int(input())
for tc in range(1, T + 1):
    n, m = map(int, input().split())
    arr = [input() for _ in range(n)]  # ???????????????????????????
    print(f'#{tc} {bfs(n, m)}')