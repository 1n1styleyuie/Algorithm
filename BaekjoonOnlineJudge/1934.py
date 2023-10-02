import sys

N = int(sys.stdin.readline())
for i in range(N):
    A, B = map(int, sys.stdin.readline().split())
    res = A * B
    while B:
        if A > B:
            A, B = B, A
        B %= A

    print(res//A)