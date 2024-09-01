# 9095 s3

import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    dp = [0] * 12

    '''
    1 : 1
    2 : 1+1, 2
    3 : 1+1+1, 2+1, 1+2, 3
    4 : 1+1+1+1, 2+1+1, 1+2+1, 3+1, 1+1+2, 2+2, 1+3

    4를 만드는 방법의 수는 3, 2, 1을 만드는 방법의 수를 더한 합니다.
    따라서 점화식은 dp[i] = dp[i-1] + dp[i-2] + dp[i-3]이 된다.
    '''

    dp[1] = 1
    dp[2] = 2
    dp[3] = 4

    for i in range(4, n+1):
        dp[i] = dp[i-1] + dp[i-2] + dp[i-3]

    print(dp[n])