# 9019 g4
import sys
input = sys.stdin.readline
from collections import deque

'''
pypy 제출 통과 문제입니다.

그래프이론, 그래프탐색, 너비우선탐색 이라고 문제분류가 되어 있지만
탐색을 하는 과정에서 이전 값을 저장을 해야 시간초과를 줄일 수 있는 문제입니다.

따라서 이전 값을 저장할 배열, 너비우선탐색을 같이 해야 풀리는 문제입니다.
'''


dslr = ['D', 'S', 'L', 'R']
def bfs(start):
    global visited
    q = deque()
    q.append(start)    
    visited[start] = 1
    while q:
        tmp = q.popleft()
        # b에 도착했을 경우 return
        if tmp == b:
            return

        for i in dslr:
            if i == 'D':
                n = (tmp * 2) % 10000
            elif i == 'S':
                if tmp > 0:
                    n = tmp - 1
                else:
                    n = 9999
            elif i == 'L':
                n = (tmp % 1000) * 10 + tmp // 1000
            else:
                n = (tmp % 10) * 1000 + tmp // 10
        
            if not visited[n]:
                visited[n] = 1
                q.append(n)
                # prev에 이전 위치와 dslr중 어떤 방법으로 움직였는지 저장
                prev[n].append([tmp, i])


t = int(input())
for _ in range(t):
    a, b = map(int, input().split())
    # 방문자 확인과 이전 위치와 dslr을 저장하기 위한 배열 생성
    visited = [0] * 10001
    prev = [[] for _ in range(10001)]
    bfs(a)
    # 역추적을 통해 b에서 a로 가는 방법을 res에 저장한다
    # prev에 이전값과 커맨드를 저장했기 때문에 이전값을 b로 바꿔가며 a일 경우까지 찾아간다.
    res = []
    while True:
        if b == int(a):
            break
        rev, cmd = prev[b][0]
        res.append(cmd)
        b = rev
    # b에서 a로의 결과값을 저장했기 때문에 reverse하여 출력
    print(''.join(reversed(res)))