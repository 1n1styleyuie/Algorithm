# 14621 g3
import sys
input = sys.stdin.readline
import heapq


def f():
    heap = []
    visited = [0] * (n+1)
    heapq.heappush(heap, (0, 1))

    total = 0
    cnt = 0
    while heap:
        weight, v = heapq.heappop(heap)
        if visited[v]:
            continue

        visited[v] = 1
        total += weight
        cnt += 1

        for next_node, next_weight in graph[v]:
            if not visited[next_node]:
                heapq.heappush(heap, (next_weight, next_node))
    
    if cnt == n:
        return total
    else:
        return -1


n, m = map(int, input().split())
arr = list(input().rstrip().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    u, v, d = map(int, input().split())
    if arr[u-1] != arr[v-1]: 
        graph[u].append((v, d))
        graph[v].append((u, d))

print(f())
