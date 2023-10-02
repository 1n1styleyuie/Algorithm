import sys
input = sys.stdin.readline

# 27918
N = int(input())
d = 0
p = 0
for _ in range(N):
    s = input().strip()
    if s == 'D':
        d += 1
    elif s == 'P':
        p += 1

    if abs(d-p) >= 2:
        break
print(f'{d}:{p}')