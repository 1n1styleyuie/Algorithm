# 1009 b2

import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    a, b = map(int, input().split())
    tmp = a % 10

    if tmp == 0:
        print(10)
    elif tmp == 1 or tmp == 5 or tmp == 6:
        print(tmp)
    elif tmp == 4 or tmp == 9:
        if b % 2 == 0:
            print((tmp ** 2) % 10)
        else:
            print(tmp)
    else:
        if b % 4 == 0:
            print(tmp ** 4 % 10)
        else:
            print(tmp ** (b % 4) % 10)