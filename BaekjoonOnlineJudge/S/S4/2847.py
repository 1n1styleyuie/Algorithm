# 2847 s4
import sys
input = sys.stdin.readline


n = int(input())
arr = [int(input()) for _ in range(n)]

res = 0
for i in range(n-2, -1, -1):
    if arr[i] >= arr[i+1]:
        res += arr[i] - arr[i+1] + 1
        arr[i] -= arr[i] - arr[i+1] + 1

print(res)