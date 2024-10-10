# 24481 s2
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def dfs(r, depth):
    # visited에 깊이 저장
    visited[r] = depth
    # 인접정점 오름차순 정렬
    adj_l[r].sort()
    for a in adj_l[r]:
        # 방문하지 않은 곳을 탐색
        if not visited[a]:
            dfs(a, depth+1)



n, m, r = map(int, input().split())
adj_l = [[] for _ in range(n+1)]
for _ in range(m):
    u, v = map(int, input().split())
    # 양방향 그래프
    adj_l[u].append(v)
    adj_l[v].append(u)

visited = [0] * (n+1)

dfs(r, 1)

for i in range(1, n+1):
    # 1을 더해주고 시작했기 떄문에 출력할 때 -1 하여 출력
    print(visited[i] - 1)