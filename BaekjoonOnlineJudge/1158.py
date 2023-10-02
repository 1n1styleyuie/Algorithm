import sys
input = sys.stdin.readline


# 1158
from collections import deque
N, K = map(int, input().split())
arr = deque([i for i in range(1, N+1)])
q = deque([])
while arr:
    for i in range(K-1):
        arr.append(arr.popleft())
    q.append(arr.popleft())

print('<', end='')
for i in range(N-1):
    print(q[i], end=', ')
print(q[-1], end='')
print('>')