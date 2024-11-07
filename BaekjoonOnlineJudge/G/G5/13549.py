# 13549 g5
import sys
input = sys.stdin.readline
from collections import deque

def bfs(n, k):
    q = deque()
    q.append(n)
    visited[n] = 1
    while q:
        x = q.popleft()
        if x == k:
            return
        # 움직이는 방법은 2*x, x-1, x+1 세가지이고
        # 2*x의 경우만 시간을 쓰지 않기 때문에 이전 값과 동일하게 visited에 저장
        for nx in (2*x, x-1, x+1):
            if 0 <= nx < 100001:
                if not visited[nx]:
                    if nx == 2*x:
                        visited[nx] = visited[x]
                    else:
                        visited[nx] = visited[x] + 1
                    q.append(nx)


n, k = map(int, input().split())
visited = [0] * 100001
bfs(n, k)
print(visited[k]-1)