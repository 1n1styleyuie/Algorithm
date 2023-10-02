import heapq


def dijkstra(start):
    # 우선순위 큐
    pq = []
    # 출발점 초기화
    heapq.heappush(pq, (0, start))
    distance[start[0]][start[1]] = 0
    while pq:
        # 현재 시점에서 누적거리가 가장 짧은 노드에 대한 정보 꺼내기
        dist, now = heapq.heappop(pq)
        # 이미 방문한 지점 + 누적거리가 더 짧게 방문한 적이 있다면 pass
        if dist > distance[now[0]][now[1]]:
            continue

        # 델타 탐색을 통해
        for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
            ni, nj = now[0] + di, now[1] + dj
            if 0 <= ni < N and 0 <= nj < N:
                # 이동 가능하면 1증가
                new_cost = dist + 1
                # 높이가 높아지면 그만큼 더 증가
                if graph[now[0]][now[1]] < graph[ni][nj]:
                    new_cost += (graph[ni][nj] - graph[now[0]][now[1]])
                # 기존보다 크다면
                if distance[ni][nj] <= new_cost:
                    continue
                distance[ni][nj] = new_cost
                heapq.heappush(pq, (new_cost, (ni, nj)))


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    graph = [list(map(int, input().split())) for _ in range(N)]
    INF = int(1e9)
    distance = [[INF] * N for _ in range(N)]
    dijkstra((0, 0))
    print(f'#{tc} {distance[N - 1][N - 1]}')

