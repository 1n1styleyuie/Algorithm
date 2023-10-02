import sys
input = sys.stdin.readline

# Kruskal
V = int(input())
E = int(input())
graph = []
for _ in range(E):
    f, t, w = map(int, input().split())
    graph.append([f, t, w])
graph.sort(key=lambda x: x[2])

parents = [i for i in range(V+1)]

def find_set(x):
    if parents[x] == x:
        return x
    return find_set(parents[x])


def union(x, y):
    x = find_set(x)
    y = find_set(y)

    if x == y:
        return

    if x < y:
        parents[y] = x
    else:
        parents[x] = y

cnt = 0
sum_weight = 0
for f, t, w in graph:
    if find_set(f) != find_set(t):
        cnt += 1
        sum_weight += w
        union(f, t)
        if cnt == V:
            break
print(sum_weight)