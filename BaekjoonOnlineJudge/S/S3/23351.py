# 23351 s3
import sys
input = sys.stdin.readline


n, k, a, b = map(int, input().split())

arr = [k] * n
res = 0
while True:

    for i in range(a):
        arr[i] += b
    
    for j in range(len(arr)):
        arr[j] -= 1

    arr.sort()
    res += 1
    if arr[0] == 0:
        print(res)
        break