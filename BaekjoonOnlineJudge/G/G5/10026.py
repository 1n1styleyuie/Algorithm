# 10026
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

delta = [[0, 1], [0, -1], [1, 0], [-1, 0]]

def dfs(i, j):
    visited[i][j] = 1
    for di, dj in delta:
        ni, nj = i+di, j+dj
        if 0<=ni<N and 0<=nj<N:
            if not visited[ni][nj]:
                if arr[ni][nj] == arr[i][j]:
                    dfs(ni, nj)


N = int(input())
arr = [list(input().strip()) for _ in range(N)]
visited = [[0] * N for _ in range(N)]
rgbcnt = 0
rgcnt = 0

for i in range(N):
    for j in range(N):
        if visited[i][j] == 0:
            dfs(i, j)
            rgbcnt += 1

for i in range(N):
    for j in range(N):
        if arr[i][j] == 'R':
            arr[i][j] = 'G'

visited = [[0] * N for _ in range(N)]
for i in range(N):
    for j in range(N):
        if visited[i][j] == 0:
            dfs(i, j)
            rgcnt += 1

print(rgbcnt, rgcnt)

