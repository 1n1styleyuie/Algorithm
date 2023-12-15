N, K = map(int, input().split())

arr = []
for _ in range(N):
    arr.append(int(input()))
arr.sort(reverse=True)

count = 0
for i in arr:
    if K >= i:
        count += K // i
        K %= i
        if K <= 0:
            break

print(count)