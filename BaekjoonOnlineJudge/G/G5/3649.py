# 3649 g5
import sys
input = sys.stdin.readline

while True:
    try:
        x = int(input()) * (10 ** 7)
        n = int(input())
        arr = []
        for _ in range(n):
            arr.append(int(input()))

        arr.sort()

        start = 0
        end = n-1
        flg = False
        while start < end:
            if arr[start] + arr[end] == x:
                flg = True
                break

            if arr[start] + arr[end] < x:
                start += 1
            else:
                end -= 1

        if flg:
            print('yes', arr[start], arr[end])
        else:
            print('danger')
    except:
        break