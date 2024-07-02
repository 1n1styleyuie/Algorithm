import sys

input = sys.stdin.readline

N = int(input())

cnt = 0
ans = 2
while True:
    if cnt == N:
        print((ans)**2)
        break
    ans = (ans+(ans-1))
    cnt += 1