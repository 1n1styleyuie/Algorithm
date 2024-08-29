# 1026 s4
import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

# a는 오름차순, b는 내림차순
a.sort()
b.sort(reverse=True)
ans = 0
# 가장 큰 수와 가장 작은수를 곱해서 더한 최종 ans가 최소가 되도록
for i in range(n):
    ans += a[i]*b[i]

print(ans)