# 5567 s2
import sys
input = sys.stdin.readline
from collections import deque


def bfs(x):
    global res
    q = deque()
    q.append((x, 0))
    visited[x] = 1
    while q:
        i, cnt = q.popleft()
        for next in arr[i]:
            # 친구의 친구까지만 찾기
            if not visited[next] and cnt < 2:
                visited[next] = 1
                q.append((next, cnt+1))
                res += 1
    


n = int(input())
m = int(input())

arr = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)

visited = [0] * (n+1)
res = 0
bfs(1)

print(res)