# 24511 s3
import sys
input = sys.stdin.readline
from collections import deque

n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
m = int(input())
c = list(map(int, input().split()))

arr = deque()
for i in range(n):
    if a[i] == 0:
        arr.appendleft(b[i])

res = []
for j in range(m):
    arr.append(c[j])
    res.append(arr.popleft())

print(*res)