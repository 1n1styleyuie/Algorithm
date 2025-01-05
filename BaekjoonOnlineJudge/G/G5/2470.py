# 2470 g5
import sys
input = sys.stdin.readline


n = int(input())
arr = list(map(int, input().split()))
arr.sort()

min_cnt = 20000000001
start = 0
end = n-1
res = [arr[start], arr[end]]

while start < end:
    if abs(arr[start] + arr[end]) < min_cnt:
        res.clear()
        res.append(arr[start])
        res.append(arr[end])
        min_cnt = abs(arr[start] + arr[end])
    if arr[start] + arr[end] < 0:
        start += 1
    else:
        end -= 1


print(*sorted(res))