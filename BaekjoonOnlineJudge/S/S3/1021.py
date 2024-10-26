# 1021 s3
import sys
input = sys.stdin.readline
from collections import deque


n, m = map(int, input().split())
a = list(map(int, input().split()))

d = deque([i for i in range(1, n+1)])

cnt = 0

for i in a:
    while True:
        if d[0] == i:
            d.popleft()
            break
        else:
            # 뽑을 위치의 인덱스가 반으로 나눈것보다 작을 경우엔 popleft하여 append
            if d.index(i) < len(d)/2 :
                while d[0] != i:
                    d.append(d.popleft())
                    cnt += 1
            # 뽑을 위치의 인덱스가 반으로 나눈것보다 클 경우엔 pop하여 appendleft
            else:
                while d[0] != i:
                    d.appendleft(d.pop())
                    cnt += 1

print(cnt)