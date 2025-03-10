# 28066 s3
import sys
input = sys.stdin.readline
from collections import deque


n, k = map(int, input().split())
arr = deque([i for i in range(1, n+1)])

while len(arr) > k:
    arr.append(arr.popleft())
    for _ in range(k-1):
        arr.popleft()

print(arr.popleft())