# 12851 g4
import sys
input = sys.stdin.readline
from collections import deque

def bfs(n, k):
    global cnt
    q = deque()
    q.append(n)
    visited[n] = 1
    while q:
        x = q.popleft()
        # 도달할때마다 cnt+1하여 가장 빠른 시간으로 찾는 방법 가짓수를 저장
        if x == k:
            cnt += 1
        # 움직이는 방법은 2*x, x-1, x+1 세가지
        # 방문하지 않은 곳이거나 방문할 곳이 visited[x]+1보다 작거나 같다면
        # 방문처리 후 q에 추가
        for nx in (2*x, x-1, x+1):
            if 0 <= nx < 100001:
                if not visited[nx] or visited[nx] >= visited[x]+1:
                    visited[nx] = visited[x] + 1
                    q.append(nx)


n, k = map(int, input().split())
visited = [0] * 100001
cnt = 0
bfs(n, k)
print(visited[k]-1)
print(cnt)