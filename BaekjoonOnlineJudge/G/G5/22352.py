# 22352 g5

import sys
input = sys.stdin.readline
from collections import deque

delta = [[0, 1], [0, -1], [1, 0], [-1, 0]]


def bfs(x, y):
    global ans
    q = deque()
    q.append((x, y))
    visited[x][y] = 1
    # 다른 값이니까 ans에 1 추가
    if before[x][y] != after[x][y]:
        ans += 1
    while q:
        i, j = q.popleft()
        for di, dj in delta:
            ni, nj = i+di, j+dj
            if 0 <= ni < n and 0 <= nj < m: 
                if before[ni][nj] == before[i][j]: # 같은 값인 경우
                    if after[ni][nj] == after[i][j] and not visited[ni][nj]:
                        visited[ni][nj] = 1
                        q.append((ni, nj))
                    if after[ni][nj] != after[i][j]:
                        # 이전 값과 다를경우 더이상 진행하지 않고 return
                        ans += 100
                        return


n, m = map(int, input().split())
before = [list(map(int, input().split())) for _ in range(n)]
after = [list(map(int, input().split())) for _ in range(n)]
visited = [[0] * m for _ in range(n)]

flg = False
ans = 0

for i in range(n):
    for j in range(m):
        if not visited[i][j]: # 방문한적 없으면 모두 방문
            bfs(i, j)
        if ans > 1: # 하나 이상 다른게 있으면 더이상 볼 필요가 없음
            flg = True
            break
    if flg:
        break

# 두개 이상 다른 값이 있을경우 NO
# 아닐 경우 YES
if ans > 1:
    print('NO')
else:
    print('YES')