# 30802 b3
import sys
input = sys.stdin.readline


n = int(input())
arr = list(map(int, input().split()))
t, p = map(int, input().split())

s = 0
for a in arr:
    if a == 0:
        continue
    elif a <= t:
        s += 1
    elif a % t == 0:
        s += a // t
    else:
        s += (a // t) + 1

print(s)
print(n//p, n%p)