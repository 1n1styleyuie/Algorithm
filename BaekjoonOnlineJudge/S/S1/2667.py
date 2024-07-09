import sys
input = sys.stdin.readline
from collections import deque

delta = [[0, 1], [0, -1], [1, 0], [-1, 0]]

def bfs(i, j):
    q = deque()
    q.append((i, j))
    visited[i][j] = 1
    cnt = 1
    while q:
        i, j = q.popleft()
        for di, dj in delta:
            ni, nj = i+di, j+dj
            if 0<=ni<N and 0<=nj<N and not visited[ni][nj]:
                if arr[ni][nj] == 1:
                    q.append((ni, nj))
                    visited[ni][nj] = 1
                    cnt += 1
    return cnt


N = int(input())
arr = [list(map(int, input().rstrip())) for _ in range(N)]
visited = [[0] * (N+1) for _ in range(N+1)]
total = 0
answer = []
for i in range(N):
    for j in range(N):
        if arr[i][j] == 1 and not visited[i][j]:
            total += 1
            answer.append(bfs(i, j))

print(total)
answer.sort()
for ans in answer:
    print(ans)