import sys
input = sys.stdin.readline


# 28295
res = 0
for _ in range(10):
    i = int(input())
    if i == 1:
        res += 1
    elif i == 2:
        res += 2
    elif i == 3:
        res -= 1

if res % 4 == 0:
    print('N')
elif res % 4 == 1:
    print('E')
elif res % 4 == 2:
    print('S')
elif res % 4 == 3:
    print('W')