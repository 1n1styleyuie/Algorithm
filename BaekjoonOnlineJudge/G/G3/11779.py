# 11779 g3
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

        for i in bus[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                # 다음 위치로 넘어갈 곳에 넘어가기 전 위치를 저장
                prev[i[0]] = now
                heapq.heappush(q, (cost, i[0]))


n = int(input())
m = int(input())
bus = [[] for _ in range(n+1)]
INF = int(1e9)
distance = [INF] * (n+1)
prev = [0] * (n+1)

for _ in range(m):
    u, v, w = map(int, input().split())
    bus[u].append((v, w))

start, end = map(int, input().split())
dijkstra(start)

path = [end]
tmp = end
# 이전 값들을 거슬러 올라가며 찾기
while tmp != start:
    tmp = prev[tmp]
    path.append(tmp)

path.reverse()

print(distance[end])
print(len(path))
print(' '.join(map(str, path)))