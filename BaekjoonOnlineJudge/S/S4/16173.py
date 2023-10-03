import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline


def dfs(i, j):
    # 델타탐색
    if i<0 or i>=N or j<0 or j>=N or visited[i][j] == 1:
        return

    if arr[i][j] == -1:
        visited[i][j] = 1
        return

    visited[i][j] = 1
    dfs(i+arr[i][j], j)
    dfs(i, j+arr[i][j])


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
visited = [[0] * N for _ in range(N)]
dfs(0, 0)

if visited[-1][-1] == 1:
    print('HaruHaru')
else:
    print('Hing')
