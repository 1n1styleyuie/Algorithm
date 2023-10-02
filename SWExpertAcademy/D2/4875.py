di = [0, 0, 1, -1]
dj = [1, -1, 0, 0]


def find_index(N):
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 2:
                return i, j


def bfs(sti, stj, N):
    visited = [[0]*(N+1) for _ in range(N+1)]
    q = []
    q.append((sti, stj))
    visited[sti][stj] = 1
    while q:
        si, sj = q.pop(0)
        if arr[si][sj] == 3:
            return 1
        for k in range(4):
            ni, nj = si+di[k], sj+dj[k]
            if 0<=ni<N and 0<=nj<N and arr[ni][nj] != 1 and visited[ni][nj] == 0:
                q.append((ni, nj))
                visited[ni][nj] = 1
    return 0


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().strip())) for _ in range(N)]
    sti, stj = find_index(N)
    ans = bfs(sti, stj, N)
    print(f'#{tc} {ans}')