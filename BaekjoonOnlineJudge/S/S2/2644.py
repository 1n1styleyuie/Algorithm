def dfs(a, b, V, adj_m):
    stack = []
    visited = [0] * (V+1)
    visited[a] = 1
    cnt = 1
    while True:
        for w in range(1, V+1):
            if adj_m[a][w] == 1:
                if visited[w] == 0:
                    stack.append(a)
                    a = w
                    visited[a] += cnt
                    cnt += 1
                    break
        else:
            if stack:
                a = stack.pop()
                cnt -= 1
            else:
                break
    if not visited[b]:
        return -1
    else:
        return visited[b]



N = int(input())
a, b = map(int, input().split())
M = int(input())
adj_m = [[0]*(N+1) for _ in range(N+1)]
for _ in range(M):
    x, y = map(int, input().split())
    adj_m[x][y] = 1
    adj_m[y][x] = 1


print(dfs(a, b, N, adj_m))