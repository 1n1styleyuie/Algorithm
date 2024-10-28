# 1753 g4
import sys
input = sys.stdin.readline
import heapq


def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)

        if distance[now] < dist: 
            continue

        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))


V, E = map(int, input().split())
k = int(input())
INF = int(1e9)
graph = [[] for _ in range(V+1)]
distance = [INF] * (V+1)

for _ in range(E):
    # 방향 그래프
    u, v, w = map(int, input().split())
    graph[u].append((v, w))

dijkstra(k)


for i in range(1, V+1):
    if distance[i] == INF:
        print('INF')
    else:
        print(distance[i])