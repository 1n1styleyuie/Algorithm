import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)


# 1245
delta = [[0, 1], [0, -1], [1, 0], [-1, 0], [-1, -1], [-1, 1], [1, -1], [1, 1]]
def dfs(i, j):
    global top
    visited[i][j] = 1
    for di, dj in delta:
        ni, nj = i+di, j+dj
        if 0<=ni<n and 0<=nj<m:
            if arr[i][j] < arr[ni][nj]:
                top = False
            if not visited[ni][nj] and arr[ni][nj] == arr[i][j]:
                dfs(ni, nj)


n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
visited = [[0]*m for _ in range(n)]
cnt = 0

for i in range(n):
    for j in range(m):
        if arr[i][j] > 0 and not visited[i][j]:
            top = True
            dfs(i, j)
            if top:
                cnt += 1

print(cnt)