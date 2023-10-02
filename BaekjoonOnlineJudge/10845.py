import sys
input = sys.stdin.readline

N = int(input())
stack = []
for _ in range(N):
    i = input().split()
    if i[0] == 'push':
        stack.append(i[1])
    elif i[0] == 'pop':
        if not stack:
            print(-1)
        else:
            print(stack.pop(0))
    elif i[0] == 'front':
        if not stack:
            print(-1)
        else:
            print(stack[0])
    elif i[0] == 'back':
        if not stack:
            print(-1)
        else:
            print(stack[-1])
    elif i[0] == 'empty':
        if stack:
            print(0)
        else:
            print(1)
    elif i[0] == 'size':
        print(len(stack))