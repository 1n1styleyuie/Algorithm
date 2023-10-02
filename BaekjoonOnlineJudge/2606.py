import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)


# 2606
def dfs(start):
    visited[start] = 1
    for i in adj_l[start]:
        if not visited[i]:
            dfs(i)


n = int(input())
m = int(input())
adj_l = [[] for _ in range(n+1)]
visited = [0]*(n+1)
for _ in range(m):
    x, y = map(int, input().split())
    adj_l[x].append(y)
    adj_l[y].append(x)

dfs(1)
print(sum(visited)-1)