import sys
input = sys.stdin.readline
from collections import deque
delta = [[0,1], [1, 0]]

def bfs():
    q = deque()
    q.append((0, 0))
    visited[0][0] = 1
    while q:
        i, j = q.popleft()
        for di, dj in delta:
            ni, nj = i+(di*arr[i][j]), j+(dj*arr[i][j])
            if 0<=ni<N and 0<= nj<N:
                if not visited[ni][nj]:
                    visited[ni][nj] = 1
                    q.append((ni, nj))
            

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
visited = [[0] * N for _ in range(N)]
bfs()
if visited[-1][-1] == 1:
    print('HaruHaru')
else:
    print('Hing')