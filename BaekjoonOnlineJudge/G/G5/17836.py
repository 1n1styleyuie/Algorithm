import sys
input = sys.stdin.readline
from collections import deque

delta = [[0, 1], [0, -1], [-1, 0], [1, 0]]

def bfs():
    q = deque()
    q.append((0, 0))
    visited = [[0] * M for _ in range(N)]
    gram = 100000
    visited[0][0] = 1
    while q:
        i, j = q.popleft()
        # 도착 했을 때 gram으로 간 것과 visited에 기록된 값 중 작은 값으로 리턴
        if (i, j) == (N-1, M-1):
            return min(visited[i][j]-1, gram)
        
        # gram으로부터 공주와의 두점사이 거리를 gram까지 온 시간에 더해서 저장
        if arr[i][j] == 2:
            gram = visited[i][j] - 1 + (N - 1 - i) + (M - 1 - j)

        for di, dj in delta:
            ni, nj = i + di, j + dj
            if 0 <= ni < N and 0 <= nj < M and not visited[ni][nj]:
                if arr[ni][nj] == 0 or arr[ni][nj] == 2:
                    visited[ni][nj] = visited[i][j] + 1
                    q.append((ni, nj))
    return gram

N, M, T = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
answer = bfs()

if answer > T:
    print('Fail')
else:
    print(answer)