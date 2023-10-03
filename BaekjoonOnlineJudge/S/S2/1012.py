import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

# 1012
delta = [[0, 1], [0, -1], [1, 0], [-1, 0]]

def dfs(sti, stj):
    for di, dj in delta:
        ni, nj = sti+di, stj+dj
        if 0<=ni<m and 0<=nj<n:
            if adj_m[nj][ni] == 1:
                adj_m[nj][ni] = 0
                dfs(ni, nj)


T = int(input())
for tc in range(T):
    m, n, k = map(int, input().split())
    adj_m = [[0]*m for _ in range(n)]
    for _ in range(k):
        x, y = map(int, input().split())
        adj_m[y][x] = 1
    cnt = 0
    for x in range(m):
        for y in range(n):
            if adj_m[y][x] == 1:
                dfs(x, y)
                cnt += 1
    print(cnt)