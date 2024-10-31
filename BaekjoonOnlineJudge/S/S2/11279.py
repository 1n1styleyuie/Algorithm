# 11279 s2
import sys
input = sys.stdin.readline
import heapq

'''
파이썬에서 힙은 최소힙을 사용한다.
따라서 최대 힙으로 되어있는 트리를 사용하고 싶다면 부호를 마이너스로 바꿔서 저장하면
최대힙으로 저장할 수 있다.
그리고 출력할 때 마이너스를 붙여서 사용하면 원래의 값을 다시 뽑아낼 수 있다.
'''

n = int(input())
q = []

for _ in range(n):
    x = int(input())
    if x > 0:
        heapq.heappush(q, -x)
    else:
        if not q:
            print(0)
        else:
            print(-heapq.heappop(q))
