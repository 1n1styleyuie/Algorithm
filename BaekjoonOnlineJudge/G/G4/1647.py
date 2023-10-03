import sys
input = sys.stdin.readline
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


V, E = map(int, input().split())
graph = []
for _ in range(E):
    f, t, w = map(int, input().split())
    graph.append([f,t,w])
graph.sort(key=lambda x: x[2])

parents = [i for i in range(V+1)]

sum_weight = 0
last = 0
for f, t, w in graph:
    if find_set(f) != find_set(t):
        sum_weight += w
        union(f, t)
        last = w
print(sum_weight-last)
