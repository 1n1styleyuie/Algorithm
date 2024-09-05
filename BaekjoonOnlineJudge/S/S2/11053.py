# 11053 s2
import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
dp = [1] * n

'''
10 20 10 30 20 50                   dp = [1, 1, 1, 1, 1, 1]

i = 1
j = 0   arr[1] > a[0] : True        dp = [1, 2, 1, 1, 1, 1]

i = 2
j = 0   arr[2] > arr[0] : False
j = 1   arr[2] > arr[1] : False     dp = [1, 2, 1, 1, 1, 1]

i = 3
j = 0   arr[3] > arr[0] : True
j = 1   arr[3] > arr[1] : True
j = 2   arr[3] > arr[2] : True      dp = [1, 2, 1, 3, 1, 1]
...
i는 현재 위치를 말하고 j는 이전 수를 말한다. 
이때 dp에는 그 수를 골랐을 때 가지는 가장 큰 수열의 길이를 말한다.
따라서 arr[i]가 arr[j] 보다 클 경우 증가하는 수열이기 때문에 
arr[j]중 가장 큰 값에 +1한 값과 현재 dp에 저장된값을 비교하여 저장하면된다.
'''

for i in range(1, n):
    for j in range(i):
        if arr[i] > arr[j]:
            dp[i] = max(dp[i], dp[j]+1)
        

print(max(dp))