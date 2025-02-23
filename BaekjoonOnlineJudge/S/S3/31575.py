# 31575 s3
import sys
input = sys.stdin.readline
from collections import deque


delta = [[0,1], [1,0]]
def bfs():
    q = deque()
    q.append((0, 0))
    visited = [[0] * n for _ in range(m)]
    visited[0][0] = 1
    while q:
        i, j = q.popleft()
        if i == m-1 and j == n-1:
            print('Yes')
            return
        for di, dj in delta:
            ni, nj = i+di, j+dj
            if 0<=ni<m and 0<=nj<n and arr[ni][nj] == 1:
                if not visited[ni][nj]:
                    q.append((ni, nj))
                    visited[ni][nj] = 1
    print('No')
    return


n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(m)]
if n == 1 and m == 1:
    print('Yes')
else:
    bfs()
