import sys
input = sys.stdin.readline
from collections import deque

delta = [[0, 1], [0, -1], [1, 0], [-1, 0]]

def bfs(x, y):
    q = deque()
    q.append((x, y))
    visited[x][y] = 1
    # 그림의 넓이를 l로 하고 1 저장
    l = 1
    while q:
        i, j = q.popleft()
        for di, dj in delta:
            ni, nj = i+di, j+dj
            if 0<=ni<n and 0<=nj<m:
                if arr[ni][nj] == 1 and not visited[ni][nj]:
                    visited[ni][nj] = 1
                    q.append((ni, nj))
                    l += 1
    # 그림의 넓이를 return
    return l


n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
# cnt : 그림의 수, max_large : 가장 넓은 그림의 넓이(단, 그림이 하나도 없을 경우 넓이는 0)
cnt = 0
max_large = 0
visited = [[0] * m for _ in range(n)]
for i in range(n):
    for j in range(m):
        # 그림인 위치와 방문하지 않은 곳을 탐색하여 bfs호출
        if arr[i][j] == 1 and not visited[i][j]:
            large = bfs(i, j)
            # 다 돌고 나온 경우 그림의 수에 +1
            cnt += 1
            # 넓이를 비교하여 가장 큰값을 저장
            max_large = max(max_large, large)

print(cnt)
print(max_large)