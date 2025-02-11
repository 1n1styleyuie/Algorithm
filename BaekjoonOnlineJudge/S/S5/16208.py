# 16208 s5
import sys
input = sys.stdin.readline


n = int(input())
arr = list(map(int, input().split()))
arr.sort()

total = sum(arr)
res = 0
for a in arr:
    total -= a
    res += a * total

print(res)