import sys
input = sys.stdin.readline
from collections import deque

a, b = map(int, input().split())
q = deque()
q.append((a, 1))

while q:
    x, cnt = q.popleft()
    # x가 b보다 크면 continue
    if x > b:
        continue
    # x == b 일경우 cnt 출력
    if x == b:
        print(cnt)
        break
    
    # 2를 곱하는 경우와 숫자 뒤에 1을 붙이는 경우를 q에 추가
    q.append((x * 2, cnt + 1))
    q.append((int(str(x) + '1'), cnt + 1))
# 찾을 수 없는 경우 -1 출력
else:
    print(-1)