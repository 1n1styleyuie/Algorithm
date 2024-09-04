# 1149 s1

import sys
input = sys.stdin.readline

'''
1 2 3
4 5 6
이렇게 주어질 경우 두번째 줄에서 이전 칸을 선택하는 방법으로 진행한다.
4를 선택할 경우 고를 수 있는 수는 2와 3뿐이기 떄문에 둘중 작은 값을 4와 더하여 dp에 저장한다.
같은 방식으로 dp에 저장 후 dp[n-1]에서 가장 작은값을 출력하면 된다.
'''

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
dp = [[0]*3 for _ in range(n)]
# 첫줄은 그대로 dp에 저장
dp[0] = arr[0]

for i in range(1, n):
    dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + arr[i][0]
    dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + arr[i][1]
    dp[i][2] = min(dp[i-1][0], dp[i-1][1]) + arr[i][2]

print(min(dp[n-1]))