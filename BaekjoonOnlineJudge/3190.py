import sys
input = sys.stdin.readline
from collections import deque


# 3190
# 상 우 하 좌
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
def f(j, i):
    if i == 'D':
        j = (j + 1) % 4
    else:
        j = (j - 1) % 4
    return j

def snake():
    direction = 1
    time = 1
    x, y = 0, 0
    visited = deque([[x, y]])
    arr[x][y] = 2
    while True:
        x, y = x+dx[direction], y+dy[direction]
        if 0<=x<N and 0<=y<N and arr[x][y] != 2:
            if arr[x][y] != 1:
                nx, ny = visited.popleft()
                arr[nx][ny] = 0
            arr[x][y] = 2
            visited.append([x, y])
            if time in t.keys():
                direction = f(direction, t[time])
            time += 1
        else:
            return time


N = int(input())
K = int(input())
arr = [[0]*N for _ in range(N)]
for _ in range(K):
    a, b = map(int, input().split())
    arr[a-1][b-1] = 1
L = int(input())
t = {}
for i in range(L):
    X, C = input().split()
    t[int(X)] = C

print(snake())