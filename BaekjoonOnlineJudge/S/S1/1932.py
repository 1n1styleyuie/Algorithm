# 1932 s1
import sys
input = sys.stdin.readline

n = int(input())
dp = [list(map(int, input().split())) for _ in range(n)]

'''
0
0   1
0   1   2
0   1   2   3
3번째 줄 0에서 고를 수 있는 이전 수는 0에 저장된 수 하나이다.
3번째 줄 1에서 고를 수 있는 이전 수는 0, 1에 저장된 수 이다.
3번째 줄 2에서 고를 수 있는 이전 수는 1에 저장된 수 하나이다.
따라서 끝점일 경우 이전줄 가장 끝점에 있는 값을 더해주고 그 외 경우 이전줄에서 올 수 있는 수 중 큰 수를 더해준다.
'''

for i in range(1, n):
    for j in range(0, i+1):
        # 왼쪽 끝점일 경우 이전 줄 왼쪽 끝점을 더해줌
        if j == 0:
            dp[i][j] += dp[i-1][0]
        # 오른쪽 끝점일 경우 이전 줄 오른쪽 끝점을 더해줌
        elif j == i:
            dp[i][j] += dp[i-1][j-1]
        # 그 외 경우 이전 줄에서 올 수 있는 수 중 큰 수를 더해줌
        else:
            dp[i][j] += max(dp[i-1][j-1], dp[i-1][j])
        
print(max(dp[n-1]))