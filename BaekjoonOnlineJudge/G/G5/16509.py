# 16509 g5
import sys
input = sys.stdin.readline
from collections import deque


delta = [
    [-1, 0, -2, -1, -3, -2], 
    [0, -1, -1, -2, -2, -3], 
    [0, -1, 1, -2, 2, -3], 
    [1, 0, 2, -1, 3, -2], 
    [1, 0, 2, 1, 3, 2],
    [0, 1, 1, 2, 2, 3], 
    [0, 1, -1, 2, -2, 3], 
    [-1, 0, -2, 1, -3, 2] 
    ]


def bfs():
    q = deque()
    q.append((r1, c1, 0))
    arr[r1][c1] = 1
    while q:
        i, j, d = q.popleft()
        if (i, j) == (r2, c2):
            return d
                
        for dx1, dy1, dx2, dy2, dx3, dy3 in delta:
            mx, my = i + dx1, j + dy1
            bx, by = i + dx2, j + dy2
            nx, ny = i + dx3, j + dy3
            
            if  0 <= mx < 10 and 0 <= my < 9 and 0 <= bx < 10 and 0 <= by < 9 and 0 <= nx < 10 and 0 <= ny < 9 and not visited[nx][ny]:
                if (mx, my) != (r2, c2) and (bx, by) != (r2, c2): 
                    visited[nx][ny] = True
                    q.append((nx, ny, d + 1))
    return -1

arr = [[0] * 9 for _ in range(10)]
r1, c1 = map(int, input().split())
r2, c2 = map(int, input().split())
visited = [[0] * 9 for _ in range(10)]
print(bfs())



