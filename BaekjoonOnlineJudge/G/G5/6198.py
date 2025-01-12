# 6198 g5
import sys
input = sys.stdin.readline


n = int(input())
arr = []
for _ in range(n):
    arr.append(int(input()))

stack = []
res = 0

for a in arr:
    while stack and stack[-1] <= a:
        stack.pop()
    res += len(stack)
    stack.append(a)

print(res)