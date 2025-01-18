# 9237 s5
import sys
input = sys.stdin.readline


n = int(input())
arr = list(map(int, input().split()))
arr.sort(reverse=True)

res = 1 + arr[0] + 1
for i in range(1, n):
    if 1 + i + arr[i] + 1 > res:
        res = 1 + i + arr[i] + 1

print(res)