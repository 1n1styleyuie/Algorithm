# 5397 s2
import sys
input = sys.stdin.readline


t = int(input())
for _ in range(t):
    ll = input().rstrip()
    res = []
    stack = []

    for l in ll:
        if l == '<':
            if res:
                stack.append(res.pop())
        elif l == '>':
            if stack:
                res.append(stack.pop())
        elif l == '-':
            if res:
                res.pop()
        else:
            res.append(l)
        
    while stack:
        res.append(stack.pop())
        
    print(''.join(res))