import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

delta = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def dfs(x, y, arr):
    arr[x][y] = '.'
    for di, dj in delta:
        nx, ny = x+di, y+dj
        if 0<=nx<h and 0<=ny<w and arr[nx][ny] == '#':
            dfs(nx, ny, arr)


T = int(input())
for tc in range(1, T+1):
    h, w = map(int, input().split())
    arr = [list(input()) for _ in range(h)]
    cnt = 0
    for i in range(h):
        for j in range(w):
            if arr[i][j] == '#':
                dfs(i, j, arr)
                cnt += 1
    print(cnt)
