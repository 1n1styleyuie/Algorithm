import heapq

def dijkstra(start):
    pq = []
    # 출발점 초기화
    heapq.heappush(pq, (0, start))
    distance[start] = 0
    while pq:
        # 현재 시점에서
        # 누적거리가 가장 짧은 노드에 대한 정보 꺼내기
        dist, now = heapq.heappop(pq)
        # 이미 방문한 지점 + 누적 거리가 더 짧게 방문한 적이 있다면 pass
        if distance[now] < dist:
            continue
        # 인접 노드를 확인
        for next in graph[now]:
            next_node = next[0]
            cost = next[1]
            # next_node로 가기 위한 누적 거리
            new_cost = dist + cost
            # 누적 거리가 기존보다 클경우
            if distance[next_node] <= new_cost:
                continue

            distance[next_node] = new_cost
            heapq.heappush(pq, (new_cost, next_node))



T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    graph = [[] for _ in range(V+1)]
    for _ in range(E):
        f, t, w = map(int, input().split())
        graph[f].append([t, w])
    INF = int(1e9)
    distance = [INF] * (V+1)
    dijkstra(0)
    print(f'#{tc} {distance[V]}')