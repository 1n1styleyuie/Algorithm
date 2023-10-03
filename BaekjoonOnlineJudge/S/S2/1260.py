import sys
input = sys.stdin.readline
from collections import deque


def dfs(start):
    visited1[start] = 1
    print(start, end=' ')
    for i in adj_l[start]:
        if not visited1[i]:
            dfs(i)


def bfs(start):
    q = deque()
    q.append(start)
    visited2[start] = 1
    while q:
        x = q.popleft()
        print(x, end=' ')
        for i in adj_l[x]:
            if not visited2[i]:
                visited2[i] = 1
                q.append(i)


N, M, V = map(int, input().split())
visited1 = [0] * (N+1)
visited2 = [0] * (N+1)
adj_l = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    adj_l[a].append(b)
    adj_l[b].append(a)

for i in adj_l:
    i.sort()

dfs(V)
print()
bfs(V)
