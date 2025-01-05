# 2467 g5
import sys
input = sys.stdin.readline


n = int(input())
arr = list(map(int, input().split()))

min_cnt = 2000000001
start = 0
end = n - 1

res = []
while start < end:
    if abs(arr[start] + arr[end]) < abs(min_cnt):
        res = [arr[start], arr[end]]
        min_cnt = abs(arr[start] + arr[end])


    if arr[start] + arr[end] < 0:
        start += 1
    else:
        end -= 1

print(*res)