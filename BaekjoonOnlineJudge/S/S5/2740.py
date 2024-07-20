#2740
n, m = map(int, input().split())

a = [list(map(int, input().split())) for _ in range(n)]

m, k = map(int, input().split())

b = [list(map(int, input().split())) for _ in range(m)]

res = [[0]*k for _ in range(n)]
for i in range(n):
    for j in range(m):
        for h in range(k):
            res[i][h] += (a[i][j] * b[j][h])

for q in range(len(res)):
    print(*res[q])