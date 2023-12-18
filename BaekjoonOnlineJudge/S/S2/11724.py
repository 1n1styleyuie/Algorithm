import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline


def dfs(i):
    visited[i] = 1
    for x in adj_l[i]:
        if not visited[x]:
            dfs(x)


N, M = map(int, input().split())

adj_l = [[] for _ in range(N+1)]

for _ in range(M):
    u, v = map(int, input().split())
    adj_l[u].append(v)
    adj_l[v].append(u)

count = 0
visited = [0]*(N+1)
for i in range(1, N+1):
    if not visited[i]:
        dfs(i)
        count += 1

print(count)