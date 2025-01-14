# 1758 s4
import sys
input = sys.stdin.readline


n = int(input())
arr = []
for _ in range(n):
    arr.append(int(input()))

arr.sort(reverse=True)

res = 0
for i in range(1, n+1):
    if arr[i-1] - (i - 1) >= 0:
        res += arr[i-1] - (i - 1)

print(res)