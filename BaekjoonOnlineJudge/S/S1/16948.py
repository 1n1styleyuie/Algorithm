# 16948 s1
import sys
input = sys.stdin.readline
from collections import deque

delta = [[-2, -1], [-2, 1], [0, -2], [0, 2], [2, -1], [2, 1]]

def bfs(r1, c1):
    q = deque()
    q.append((r1, c1))
    # 처음 시작 위치의 arr값을 0으로 저장
    arr[r1][c1] = 0
    while q:
        r, c = q.popleft()
        # 목적지에 도착했다면 return
        if r == r2 and c == c2:
            return

        for dr, dc in delta:
            nr, nc = r+dr, c+dc
            if 0<=nr<n and 0<=nc<n:
                # 최초로 방문하는 곳이라면 q에 nr, nc를 저장하고
                # 이전 지점값에 +1 하여 arr[nr][nc]에 저장
                if arr[nr][nc] == -1:
                    q.append((nr, nc))
                    arr[nr][nc] = arr[r][c]+1
                # 최초로 방문하는 곳이 아니기 때문에
                # 값을 비교해서 현재 방문할 때 이동한 횟수가 저장되어 있는 값보다 작다면
                # q에 nr, nc를 저장하고 이전 지점 값에 +1 하여 arr[nr][nc]에 저장
                else:
                    if arr[r][c]+1 < arr[nr][nc]:
                        q.append((nr, nc))
                        arr[nr][nc] = arr[r][c]+1
    return



n = int(input())
r1, c1, r2, c2 = map(int, input().split())
# arr를 -1로 저장
arr = [[-1] * n for _ in range(n)]

bfs(r1, c1)
# -1로 초기값을 저장했기 때문에 도달할 수 없다면 -1이 출력되고 도달했다면 최소 이동 횟수를 출력한다.
print(arr[r2][c2])