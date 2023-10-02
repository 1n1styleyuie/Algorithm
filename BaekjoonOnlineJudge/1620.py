import sys

input = sys.stdin.readline

N, M = map(int, input().split())
poketmon = {}
idx = {}
for i in range(1, N + 1):
    a = input().strip()
    poketmon[a] = i
    idx[i] = a

for _ in range(M):
    b = input().strip()
    if b.isdigit():
        print(idx[int(b)])
    else:
        print(poketmon[b])