# 15558 g5
import sys
input = sys.stdin.readline
from collections import deque


def bfs():
    delta = [[0, 1], [0, -1], [1, k], [-1, k]]
    q = deque()
    q.append((0, 0, 0))
    visited = [[0] * n for _ in range(2)]
    while q:
        i, j, time = q.popleft()
        for di, dj in delta:
            ni, nj = i+di, j+dj
            if nj >= n:
                print(1)
                exit()

            if 0 <= ni < 2 and time < nj < n and arr[ni][nj] == 1 and not visited[ni][nj]:
                q.append((ni, nj, time + 1))
                visited[ni][nj] = 1
                    
    print(0)


n, k = map(int, input().rstrip().split())
arr = [list(map(int, input().rstrip())) for _ in range(2)]
bfs()