# 2217 s5
import sys
input = sys.stdin.readline


n = int(input())
arr = [int(input()) for _ in range(n)]
arr.sort(reverse=True)

res = 0
for i in range(n):
    if arr[i] * (i+1) > res:
        res = arr[i] * (i+1)

print(res)