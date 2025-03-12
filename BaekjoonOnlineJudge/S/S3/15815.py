# 15815 s3
import sys
input = sys.stdin.readline


arr = list(input().rstrip())

stack = []

for a in arr:
    if a == '+':
        x = stack.pop()
        y = stack.pop()
        stack.append(x+y)
    elif a == '-':
        x = stack.pop()
        y = stack.pop()
        stack.append(y-x)
    elif a == '*':
        x = stack.pop()
        y = stack.pop()
        stack.append(x*y)
    elif a == '/':
        x = stack.pop()
        y = stack.pop()
        stack.append(y//x)
    else:
        stack.append(int(a))
    
print(*stack)