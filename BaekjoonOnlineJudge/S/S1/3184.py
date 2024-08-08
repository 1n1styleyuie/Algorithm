# 3174 s1

import sys
input = sys.stdin.readline
from collections import deque

delta = [[0, 1], [0, -1], [1, 0], [-1, 0]]
def bfs(x, y):
    q = deque()
    q.append((x, y))
    visited[x][y] = 1
    o = 0
    v = 0
    # 양, 늑대 숫자 카운트
    if arr[x][y] == 'v':
        v += 1
    if arr[x][y] == 'o':
        o += 1
    while q:
        i, j = q.popleft()
        for di, dj in delta:
            ni, nj = i+di, j+dj
            if 0<=ni<r and 0<=nj<c:
                # 벽이 아니고 방문하지 않은 곳일 경우
                if arr[ni][nj] != '#' and not visited[ni][nj]:
                    q.append((ni, nj))
                    visited[ni][nj] = 1
                    if arr[ni][nj] == 'v':
                        v += 1
                    if arr[ni][nj] == 'o':
                        o += 1
    # 양이 많을 경우 o, 0 리턴
    # 그 외 0, v 리턴
    if o > v:
        return o, 0
    else:
        return 0, v
                    

r, c = map(int, input().split())
arr = [list(input()) for _ in range(r)]
visited = [[0] * c for _ in range(r)]
o_cnt = 0
v_cnt = 0
for i in range(r):
    for j in range(c):
        # 벽이 아닌곳과 방문하지 않은 곳
        if arr[i][j] != '#' and not visited[i][j]:
            o, v = bfs(i, j)
            # 전체 카운트에 추가
            o_cnt += o
            v_cnt += v

print(o_cnt, v_cnt)