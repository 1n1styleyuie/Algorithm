import sys
sys.setrecursionlimit(10**7)

delta = [[0, 1], [0, -1], [1, 0], [-1, 0]]
def dfs(i, j):
    global count

    for di, dj in delta:
        ni, nj = i+di, j+dj
        if 0<=ni<N and 0<=nj<M and not visited[ni][nj] and arr[ni][nj] in ('P', 'O'):
            if arr[ni][nj] == 'P':
                count += 1
            visited[ni][nj] = 1
            dfs(ni, nj)


N, M = map(int, input().split())

arr = [list(input()) for _ in range(N)]

visited = [[0]*M for _ in range(N)]
count = 0
for i in range(N):
    for j in range(M):
        if arr[i][j] == 'I':
            visited[i][j] = 1
            dfs(i, j)

if count == 0:
    print('TT')
else:
    print(count)