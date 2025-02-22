# 3182 s3
import sys
input = sys.stdin.readline


n = int(input())
arr = [0]
for _ in range(n):
    arr.append(int(input()))

idx = 1
res = 0
for i in range(1, n+1):
    cnt = 0
    visited = [0] * (n+1)
    tmp = i
    visited[i] = 1
    while True:
        if not visited[arr[tmp]]:
            visited[arr[tmp]] = 1
            tmp = arr[tmp]
            cnt += 1
        else:
            break

    if res < cnt:
        idx = i
        res = cnt

print(idx)
