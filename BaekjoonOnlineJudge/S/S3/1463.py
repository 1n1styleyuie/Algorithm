# 1463 s3
import sys
input = sys.stdin.readline

n = int(input())
dp = [0] * 1000001

# 아래에서 위로 계산
for i in range(2, n+1):
    # 1을 빼는 경우
    dp[i] = dp[i-1] + 1

    # 2를 나누는 경우
    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i//2]+1)
    
    # 3을 나누는 경우
    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i//3]+1)
    
print(dp[n])