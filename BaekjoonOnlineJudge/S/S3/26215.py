# 26215 s3
import sys
input = sys.stdin.readline


n = int(input())
arr = list(map(int, input().split()))
arr.sort(reverse=True)
time = 0

if arr[0] > 1440:
    print(-1)
    exit()

if n == 1:
    if arr[0] > 1440:
        print(-1)
    else:
        print(arr[0])
    exit()

while True:
    if len(arr) > 2:
        if arr[0] != 0:
            arr[0] -= 1

        
        if arr[1] != 0:
            arr[1] -= 1

    else:
        if arr[0] != 0:
            arr[0] -= 1

        
        if arr[1] != 0:
            arr[1] -= 1

    arr.sort(reverse=True)
    time += 1        
    if arr[0] == 0:
        break


if time > 1440:
    print(-1)
else:
    print(time)