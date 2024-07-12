from collections import deque
import sys
input = sys.stdin.readline

delta = [[0, 1], [0, -1], [1, 0], [-1, 0]]

N, M = map(int, input().split())
arr = [list(map(int, input().rstrip())) for _ in range(N)]
visited = [[[0] * 2 for _ in range(M)] for _ in range(N)]


def bfs():
    q = deque()
    q.append((0, 0, 0))
    visited[0][0][0] = 1

    while q:
        i, j, k = q.popleft()

        if i == N-1 and j == M-1:
            return visited[i][j][k]
        
        for di, dj in delta:
            ni, nj = i+di, j+dj
            if 0<=ni<N and 0<=nj<M:
                # 벽을 부술수 있는 기회가 있을 경우
                if arr[ni][nj] == 1 and k == 0:
                    visited[ni][nj][1] = visited[i][j][0] + 1
                    q.append((ni, nj, 1))
                # 그 외 경우
                elif arr[ni][nj] == 0 and not visited[ni][nj][k]:
                    visited[ni][nj][k] = visited[i][j][k] + 1
                    q.append((ni, nj, k))
    return -1

print(bfs())