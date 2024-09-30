# 1966 s3
import sys
from collections import deque
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    q = deque(list(map(int, input().split())))
    
    cnt = 1

    while q:
        # 현재 큐에 있는 가장 큰 값보다 작으면 뒤로 보내기
        if q[0] < max(q):
            q.append(q.popleft())
        else:
            # 만약 찾던 값이라면 break
            if m == 0:
                break
            
            # 찾던 값이 아니지만 중요도가 높은 문서이기 때문에 pop
            q.popleft()
            # pop 횟수 카운트
            cnt += 1

        # 찾으려고 하는 문서의 위치 이동
        # 0보다 클 경우 -1해주면서 이동, 만약 0일 경우 맨 뒤로 가기 때문에 현재 배열의 길이에서 -1
        if m > 0:
            m -= 1
        else:
            m = len(q)-1
    print(cnt)

