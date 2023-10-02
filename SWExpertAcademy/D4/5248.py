def dfs(visited, adj_l, i):
    visited[i] = 1
    for j in adj_l[i]:
        if not visited[j]:
            dfs(visited, adj_l, j)


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    visited = [0] * (N+1)
    adj_l = [[] for _ in range(N+1)]
    for i in range(M):
        a1, a2 = arr[i*2], arr[i*2+1]
        adj_l[a1].append(a2)
        adj_l[a2].append(a1)
    cnt = 0
    for i in range(1, N+1):
        if not visited[i]:
            cnt += 1
            dfs(visited, adj_l, i)

    print(f'#{tc} {cnt}')