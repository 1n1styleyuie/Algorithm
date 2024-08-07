# 1303 s1

import sys
input = sys.stdin.readline
from collections import deque

delta = [[0, 1], [0, -1], [1, 0], [-1, 0]]

def bfs(x, y, p):
    q = deque()
    q.append((x, y))
    cnt = 1
    visited[x][y] = 1
    while q:
        i, j = q.popleft()
        for di, dj in delta:
            ni, nj = i+di, j+dj
            if 0 <= ni < n and 0 <= nj < m:
                if visited[ni][nj] == 0 and arr[ni][nj] == p:
                    q.append((ni, nj))
                    visited[ni][nj] = 1
                    cnt += 1
    return cnt

# m은 가로, n은 세로
m, n = map(int, input().split())
arr = [list(input()) for _ in range(n)]
visited = [[0] * m for _ in range(n)]
w_cnt = 0
b_cnt = 0
for i in range(n):
    for j in range(m):
        if not visited[i][j]:
            cnt = bfs(i, j, arr[i][j])
            if arr[i][j] == 'W':
                w_cnt += (cnt ** 2)
            if arr[i][j] == 'B':
                b_cnt += (cnt ** 2)

print(w_cnt, b_cnt)