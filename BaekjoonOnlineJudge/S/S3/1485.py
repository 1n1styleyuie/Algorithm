# 1485 s3
import sys
input = sys.stdin.readline


def cal(a, b):
    ax, ay = a[0], a[1]
    bx, by = b[0], b[1]
    return ((bx - ax) ** 2 + (by - ay) ** 2)


t = int(input())
for _ in range(t):
    arr = [list(map(int, input().split())) for _ in range(4)]
    arr.sort()

    if (cal(arr[0], arr[1]) == cal(arr[0], arr[2]) == cal(arr[1], arr[3]) == cal(arr[2], arr[3])) and (cal(arr[0], arr[3]) == cal(arr[1], arr[2])):
        print(1)
    else:
        print(0)
    