# 29155 s3
import sys
input = sys.stdin.readline


n = int(input())
p = list(map(int, input().split()))
arr = [[] for _ in range(5)]
for _ in range(n):
    k, t = map(int, input().split())
    arr[k-1].append(t)


time = 0


for i in range(5):
    arr[i].sort()
    time += arr[i][0]
    if p[i] > 1:
        for j in range(1, p[i]):
            if arr[i][j-1] == arr[i][j]:
                time += arr[i][j]
            else:
                time += arr[i][j] - arr[i][j-1]
                time += arr[i][j]
    if i < 4:
        time += 60

print(time)
