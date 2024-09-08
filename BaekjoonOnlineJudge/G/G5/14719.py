# 14719 g5
import sys
input = sys.stdin.readline


h, w = map(int, input().split())
arr = list(map(int, input().split()))
ans = 0

'''
현재 위치에서 좌우에 있는 가장 높은 값 을 찾고
그 중 작은 값을 찾아서 현재 위치보다 높은 곳이라면 ans에 더해주는 방법으로 해결
'''

for i in range(1, w-1):
    l = max(arr[:i])
    r = max(arr[i+1:])
    t = min(l, r)
    if t > arr[i]:
        ans += t - arr[i]

print(ans)