# 2750 b2
import sys
input = sys.stdin.readline

n = int(input())
arr = []
for _ in range(n):
    arr.append(int(input()))

arr.sort()
for a in arr:
    print(a)