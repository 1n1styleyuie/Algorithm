# 7562 s1
import sys
input = sys.stdin.readline
from collections import deque

knight = [[-2, -1], [-1, -2], [-2, 1], [-1, 2], [2, -1], [1, -2], [2, 1], [1, 2]]

def bfs(i, j):
    q = deque()
    q.append((i, j))
    visited[i][j] = 1
    while q:
        x, y = q.popleft()

        if x == e1 and y == e2:
            break

        for dx, dy in knight:
            nx, ny = x+dx, y+dy
            if 0<=nx<l and 0<=ny<l:
                if not visited[nx][ny]:
                    visited[nx][ny] = visited[x][y] + 1
                    q.append((nx, ny))


t = int(input())
for _ in range(t):
    l = int(input())
    arr = [[0] * l for _ in range(l)]
    s1, s2 = map(int, input().split())
    e1, e2 = map(int, input().split())

    visited = [[0] * l for _ in range(l)]

    bfs(s1, s2)
    print(visited[e1][e2] - 1)
