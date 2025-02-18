# 17952 s3
import sys
input = sys.stdin.readline


n = int(input())
stack = []
res = 0
for _ in range(n):
    arr = list(map(int, input().split()))
    if arr[0] == 1:
        stack.append((arr[1], arr[2]))
    
    if stack:
        score, time = stack.pop()
        time -= 1

        if time == 0:
            res += score
        else:
            stack.append((score, time))

print(res)