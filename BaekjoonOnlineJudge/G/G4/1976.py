# 1976 g4
import sys
input = sys.stdin.readline
from collections import deque


def bfs(start):
    q = deque()
    q.append(start)
    visited[start] = 1
    while q:
        now = q.popleft()
        for i in range(n):
            # 갈 수 있는 위치인지와 방문하지 않은 경우에만 방문
            if arr[now][i] and not visited[i]:
                visited[i] = 1
                q.append(i)

n = int(input())
m = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
trip = list(map(int, input().split()))

visited = [0] * (n+1)
# trip에서 시작은 1로 되어있지만 arr에 저장된 인덱스는 0번부터 시작이기 때문에 
# 시작지점에서 -1하여 시작
bfs(trip[0] - 1)

ans = 'YES'
# 방문하지 않은 곳이 있다면 ans 는 NO
for t in trip:
    if not visited[t-1]:
        ans = 'NO'
        break

print(ans)