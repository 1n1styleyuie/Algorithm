import heapq
import sys

input = sys.stdin.readline


def dijkstra(start):
    pq = []
    # 출발점 초기화, 단 처음 시작값을 집어 넣은 상태로
    heapq.heappush(pq, (graph[0][0], start))
    distance[start[0]][start[1]] = graph[0][0]
    while pq:
        # 현재 시점에서 누적거리가 가장 짧은 노드에 대한 정보 꺼내기
        dist, now = heapq.heappop(pq)
        # 이미 방문한 지점+크기가 더 짧게 방문한 적이 있다면
        if distance[now[0]][now[1]] < dist:
            continue
        # 델타 탐색
        for di, dj in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
            ni, nj = now[0] + di, now[1] + dj

            if 0 <= ni < N and 0 <= nj < N:
                # 이동 가능한 곳이라면 이전 크기에 더하기
                new_cost = dist + graph[ni][nj]
                # 기존보다 크다면
                if distance[ni][nj] <= new_cost:
                    continue

                distance[ni][nj] = new_cost
                heapq.heappush(pq, (new_cost, (ni, nj)))


# 테스트케이스
tc = 0
while True:
    N = int(input())
    # 종료 조건
    if N == 0:
        break
    graph = [list(map(int, input().split())) for _ in range(N)]
    INF = int(1e9)
    distance = [[INF] * N for _ in range(N)]
    # 시작지점은 0, 0
    dijkstra((0, 0))
    tc += 1
    # 마지막 도착지점의 값 출력
    print(f'Problem {tc}: {distance[N - 1][N - 1]}')