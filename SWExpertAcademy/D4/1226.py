def find_start(N):
    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:  # 시작점을 찾아 반환
                return i, j


def bfs(sti, stj, N):
    visited = [[0] * N for _ in range(N)]  # visited 생성
    q = []  # q 생성
    q.append((sti, stj))  # 시작점 enq
    visited[sti][stj] = 1  # 시작점 enq 표시
    while q:  # q가 비어있지 않으면
        i, j = q.pop(0)  # deq
        if maze[i][j] == 3:  # 처리
            return 1
        # 인접하고 enq된 적이 없으면
        # enq, enq표시
        for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
            ni, nj = i + di, j + dj
            # 범위를 벗어나지 않고 방문하지 않은 곳을 찾아서 추가
            if 0 <= ni < N and 0 <= nj < N and maze[ni][nj] != 1 and visited[ni][nj] == 0:
                q.append((ni, nj))
                visited[ni][nj] = 1
    return 0


for tc in range(1, 11):
    test_case = int(input())
    maze = [list(map(int, input())) for _ in range(16)]
    # 시작 지점을 찾아서 받아줄 변수 설정 후 함수 호출
    sti, stj = find_start(16)
    # 값을 받을 변수를 설정 하고 함수 호출
    ans = bfs(sti, stj, 16)
    print(f'#{tc} {ans}')