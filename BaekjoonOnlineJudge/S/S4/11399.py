# 11399 s4
import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

arr.sort()
ans = 0
# 대기 시간까지 더하여 계산
for i in range(n):
    ans += sum(arr[:i+1])

print(ans)