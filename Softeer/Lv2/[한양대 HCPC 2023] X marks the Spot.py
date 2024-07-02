import sys

input = sys.stdin.readline

N = int(input())
answer = ''

for _ in range(N):
    S, T = input().split()
    s1 = S.upper()
    t1 = T.upper()
    idx = s1.find('X')
    answer += t1[idx]

print(answer)