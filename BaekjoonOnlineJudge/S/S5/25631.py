# 25631 s5
import sys
input = sys.stdin.readline


n = int(input())
a = list(map(int, input().split()))
a.sort()

res = 0
while len(a) > 0:
    tmp = set(a)
    for t in tmp:
        a.remove(t)
    res += 1

print(res)