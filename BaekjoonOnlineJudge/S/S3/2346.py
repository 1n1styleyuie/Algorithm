# 2346 s3
import sys
input = sys.stdin.readline
from collections import deque

n = int(input())
num = input().split()

arr = deque()
# 인덱스 넣어서 arr에 저장
for i in range(1, n+1):
    arr.append((i, int(num[i-1])))

res = []
while 1 < len(arr):
    idx, move = arr.popleft()
    res.append(idx)
    # 움직이는 방향에 따라서
    if move < 0:
        for _ in range(abs(move)):
            arr.appendleft(arr.pop())

    else:
        for _ in range(move-1):
            arr.append(arr.popleft())

idx, move = arr.popleft()
res.append(idx)
print(*res)
