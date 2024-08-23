# 2579 s3
import sys
input = sys.stdin.readline


n = int(input())
stairs = [0] * 301
for i in range(1, n+1):
    stairs[i] = int(input())

dp = [0] * 301
# 1, 2, 3의 결과값을 미리 저장
dp[1] = stairs[1]
dp[2] = stairs[1] + stairs[2]
dp[3] = max(stairs[1] + stairs[3], stairs[2] + stairs[3])

for i in range(4, n+1):
    '''
    연속된 세개의 계단을 밟아서는 안된다고 했기 때문에 두 계단씩 연속으로 오르는건 가능하다.
    하지만 한 계단씩 연속으로 올라오는 것은 불가능하다.
    따라서 한 계단을 올라올 경우 이전에 두 계단을 올라오는 경우여야 한다.

    두 계단을 올라오는 경우 : dp[i-2] + stairs[i]
    한 계단을 올라오는 경우 : dp[i-3] + stairs[i-1] + stairs[i]    
    '''
    dp[i] = max(dp[i-2] + stairs[i], dp[i-3] + stairs[i-1] + stairs[i])

print(dp[n])