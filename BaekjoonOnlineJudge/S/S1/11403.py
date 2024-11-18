# 1347 s2
import sys
input = sys.stdin.readline
from collections import deque


def bfs(i):
    q = deque()
    q.append(i)
    visited = [0] * n
    while q:
        x = q.popleft()
        for j in range(n):
            # 아직 가보지 않은 곳이며 이동 가능한 곳일 경우
            if visited[j] == 0 and graph[x][j] == 1:
                visited[j] = 1
                res[i][j] = 1
                q.append(j)


n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]

res = [[0] * n for _ in range(n)]

for i in range(n):
    bfs(i)

for r in res:
    print(*r)