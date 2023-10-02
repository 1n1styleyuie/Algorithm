def bfs(s, g, V): # 시작정점 s, 마지막 정점 v
    visited = [0] * (V+1) # visited 생성
    q = [] # 큐 생성
    q.append(s) # 시작점 인큐
    visited[s] = 1 # 시작점 방문 표시
    while q: # 큐에 정점이 남아있으면
        t = q.pop(0) # deq
        for w in range(1, V+1):# 인접한 정점 중 인큐되지 않은 정점 w가 있으면
            if adj_m[t][w] == 1 and visited[w] == 0: # w enq, enq되었음을 표시
                q.append(w) # enq
                visited[w] = visited[t] + 1
    if visited[g] == 0:
        return 1
    else:
        return visited[g]

T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split()) # 1번부터 V번 정점, E개의 간선
    # 인접리스트
    adj_m = [[0] * (V+1) for _ in range(V+1)]
    for i in range(E):
        v1, v2 = map(int, input().split())
        adj_m[v1][v2] = 1
        adj_m[v2][v1] = 1
    S, G = map(int, input().split())
    res = bfs(S, G, V)
    print(f'#{tc}',res-1)