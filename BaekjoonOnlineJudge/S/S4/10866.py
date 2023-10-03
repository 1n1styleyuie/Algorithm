import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
dequeue = deque([])

for _ in range(N):
    i = input().split()
    if i[0] == 'push_back':
        dequeue.append(i[1])
    elif i[0] == 'push_front':
        dequeue.appendleft(i[1])
    elif i[0] == 'pop_front':
        if not dequeue:
            print(-1)
        else:
            print(dequeue.popleft())
    elif i[0] == 'pop_back':
        if not dequeue:
            print(-1)
        else:
            print(dequeue.pop())
    elif i[0] == 'front':
        if not dequeue:
            print(-1)
        else:
            print(dequeue[0])
    elif i[0] == 'back':
        if not dequeue:
            print(-1)
        else:
            print(dequeue[-1])
    elif i[0] == 'empty':
        if dequeue:
            print(0)
        else:
            print(1)
    elif i[0] == 'size':
        print(len(dequeue))