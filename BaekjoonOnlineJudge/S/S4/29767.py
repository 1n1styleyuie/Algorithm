import sys
input = sys.stdin.readline

n, k = map(int, input().split())
arr = list(map(int, input().split()))

dp = [0] * (n)
dp[0] = arr[0]
for i in range(1, n):
    dp[i] = dp[i-1] + arr[i]
    
res = 0
dp.sort(reverse=True)
for i in range(k):
    res += dp[i]
    
print(res)