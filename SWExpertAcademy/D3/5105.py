def find_start(N):
    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                return i, j


def bfs(sti, stj, N):
    visited = [[0] * N for _ in range(N)] # visited 생성
    q = [] # q 생성
    q.append((sti, stj)) # 시작점 enq
    visited[sti][stj] = 1 # 시작점 enq 표시
    while q: # q가 비어있지 않으면
        i, j = q.pop(0) # deq
        if maze[i][j] == 3: # 처리
            return visited[i][j]-2 # 지나온 칸 수 리턴
        # 인접하고 enq된 적이 없으면
        # enq, enq표시
        for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
            ni, nj = i+di, j+dj
            if 0<=ni<N and 0<=nj<N and maze[ni][nj]!=1 and visited[ni][nj] == 0:
                q.append((ni, nj))
                visited[ni][nj] = visited[i][j] + 1
    return 0 # 3인 칸에 도달할 수 없는 경우


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    maze = [list(map(int, input())) for _ in range(N)]
    sti, stj = find_start(N)
    ans = bfs(sti, stj, N)
    print(f'#{tc} {ans}')