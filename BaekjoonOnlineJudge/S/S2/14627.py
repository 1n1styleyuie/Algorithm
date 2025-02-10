# 14627 s2
import sys
input = sys.stdin.readline


s, c = map(int, input().split())
arr = []
for _ in range(s):
    arr.append(int(input()))

start = 1
end = 10e9

res = 0
while start <= end:
    mid = (start + end) // 2

    cnt = 0
    for a in arr:
        cnt += a // mid
    
    if cnt >= c:
        res = max(res, mid)
        start = mid + 1
    else:
        end = mid - 1

total = sum(arr) - (c * res)
print(int(total))