chess = [1, 1, 2, 2, 2, 8]
arr = list(map(int, input().split()))
res = []
for i in range(6):
    res.append(chess[i]-arr[i])

print(*res)