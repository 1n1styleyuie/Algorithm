# 12789 s3
import sys
input = sys.stdin.readline
from collections import deque


n = int(input())
arr = deque(list(map(int, input().split())))
stack = []

idx = 1
while arr:
    if arr[0] == idx:
        arr.popleft()
        idx += 1
    else:
        stack.append(arr.popleft())

    while stack:
        if stack[-1] == idx:
            stack.pop()
            idx += 1
        else:
            break

if not stack:
    print('Nice')
else:
    print('Sad')