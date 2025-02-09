# 5427 g4
import sys
input = sys.stdin.readline
from collections import deque


delta = [[0, 1], [0, -1], [1, 0], [-1, 0]]
def bfs():
    q = deque()
    f = deque()
    for i in range(h):
        for j in range(w):
            if arr[i][j] == '*':
                f.append((i, j, 0))
            elif arr[i][j] == '@':
                q.append((i, j, 0))
                visited[i][j] = 1
    cnt = 0
    while q:
        # cnt는 1초가 지난 시간을 의미. 
        # 즉 cnt가 2초일 경우 1초인 화재위치를 확산시킬 수 있도록 while문 조건에 추가
        cnt += 1
        while f and f[0][2] < cnt:
            i, j, time = f.popleft()
            for di, dj in delta:
                ni, nj = i + di, j + dj
                if 0 <= ni < h and 0 <= nj < w:
                    if arr[ni][nj] == '.' or arr[ni][nj] == '@':
                        arr[ni][nj] = '*'
                        f.append((ni, nj, time + 1))
        
        while q and q[0][2] < cnt:
            i, j, time = q.popleft()
            for di, dj in delta:
                ni, nj = i + di, j + dj
                if 0 <= ni < h and 0 <= nj < w:
                    if arr[ni][nj] == '.' and not visited[ni][nj]:
                        visited[ni][nj] = 1
                        q.append((ni, nj, time + 1))
                else:
                    return cnt
    
    return 'IMPOSSIBLE'


t = int(input())
for _ in range(t):
    w, h = map(int, input().split())
    arr = [list(input().rstrip()) for _ in range(h)]
    visited = [[0] * w for _ in range(h)]
    print(bfs())