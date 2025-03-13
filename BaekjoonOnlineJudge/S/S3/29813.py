# 29813 s3
import sys
input = sys.stdin.readline
from collections import deque


n = int(input())
arr = deque()
for _ in range(n):
    initial, number = input().rstrip().split()
    arr.append((initial, number))


while len(arr) > 1:
    init, num = arr.popleft()
    for _ in range(int(num)-1):
        arr.append(arr.popleft())
    arr.popleft()

print(arr[0][0])