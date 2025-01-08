# 13305 s3
import sys
input = sys.stdin.readline


n = int(input())
road = list(map(int, input().split()))
cost = list(map(int, input().split()))


res = cost[0] * road[0]
min_cost = cost[0]

for i in range(1, n-1):
    if cost[i] < min_cost:
        min_cost = cost[i]
    res += min_cost * road[i]

print(res)