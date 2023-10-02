import heapq


# 시작점, 도착점
def dijkstra(f, t):
    pq = []
    INF = int(1e9)
    distance = [INF] * (V + 1)
    heapq.heappush(pq, (0, f))
    distance[f] = 0
    while pq:
        dist, now = heapq.heappop(pq)
        if distance[now] < dist:
            continue
        # 인접 노드를 확인하기 전 이미 도달 했다면
        # 위치의 distance를 반환
        if now == t:
            return distance[t]

        for next in graph[now]:
            next_node = next[0]
            cost = next[1]
            new_cost = dist + cost
            if distance[next_node] <= new_cost:
                continue
            distance[next_node] = new_cost
            heapq.heappush(pq, (new_cost, next_node))


T = int(input())
for tc in range(1, T + 1):
    V, E, X = map(int, input().split())
    graph = [[] for i in range(V + 1)]
    for _ in range(E):
        f, t, w = map(int, input().split())
        graph[f].append([t, w])

    lst = []
    for i in range(1, V + 1):
        res = 0
        # 자기 자신은 찾을 필요가 없다.
        if i != X:
            res = dijkstra(i, X) + dijkstra(X, i)
            lst.append(res)
    print(f'#{tc} {max(lst)}')