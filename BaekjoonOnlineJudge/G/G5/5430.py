# 5567 s2
import sys
input = sys.stdin.readline
from collections import deque

t = int(input())
for _ in range(t):
    p = input().rstrip()
    n = int(input())
    s = input().rstrip()
    # 덱으로 저장하는데 앞뒤에 있는 대괄호를 제거하고 저장
    arr = deque(list(s[1:-1].split(',')))
    
    # 리버스는 +1를 하면서 체크를 하고 flg를 통해 에러를 확인
    rev = 0
    flg = False

    # n이 0이면 큐에 아무것도 존재하지 않는다.
    if n == 0:
        arr = []
    
    for i in p:
        # R일 경우 rev+1을 통해 리버스
        if i == 'R':
            rev += 1
        elif i == 'D':
            if len(arr) < 1:
                flg = True
                print('error')
                break
            else:
                # rev가 짝수면 앞에서 pop, 홀수면 뒤에서 pop
                if rev % 2 == 0:
                    arr.popleft()
                else:
                    arr.pop()
    
    if not flg:
        if rev % 2 == 0:
            print('[' + ','.join(arr) + ']')
        else:
            arr.reverse()
            print('[' + ','.join(arr) + ']')
