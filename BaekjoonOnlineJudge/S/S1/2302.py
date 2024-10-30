# 10157 s3
import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
number = [int(input()) for _ in range(m)]
dp = [0] * 41

dp[0] = 1
dp[1] = 1
dp[2] = 2
dp[3] = 3
for i in range(4, n+1):
    dp[i] = dp[i-1] + dp[i-2]

res = 1

if m > 0:
    tmp = 0
    for num in number:
        res *= dp[num-1-tmp]
        tmp = num
    res *= dp[n-tmp]
else:
    res = dp[n]

print(res)