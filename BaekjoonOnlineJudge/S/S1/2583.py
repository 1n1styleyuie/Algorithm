# 2583 s1

import sys
input = sys.stdin.readline
from collections import deque

delta = [[0, 1], [0, -1], [1, 0], [-1, 0]]

def bfs(x, y):
    q = deque()
    q.append((x, y))
    visited[x][y] = 1
    # 채운 부분의 시작 넓이를 1
    l = 1
    while q:
        i, j = q.popleft()
        for di, dj in delta:
            ni, nj = i+di, j+dj
            if 0<=ni<n and 0<=nj<m:
                if arr[ni][nj] == 0 and not visited[ni][nj]:
                    visited[ni][nj] = 1
                    q.append((ni, nj))
                    l += 1
    return l


m, n, k = map(int, input().split())
arr = [[0]* m for _ in range(n)]

# 영역을 1로 채우기
for _ in range(k):
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(x1, x2):
        for j in range(y1, y2):
            arr[i][j] = 1

cnt = 0
res = []
visited = [[0] * m for _ in range(n)]

# 0인곳을 찾아서 bfs()
for i in range(n):
    for j in range(m):
        if arr[i][j] == 0 and not visited[i][j]:
            res.append(bfs(i, j))
            cnt += 1

# 오름차순 정렬후 출력
print(cnt)
res.sort()
print(*res)