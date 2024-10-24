# 18429 s3
import sys
input = sys.stdin.readline

def f(day, weight):
    global res
    # 500이 넘지 않으면 return
    if weight < 500:
        return
    # n일만큼 운동을 완료 했다면 res + 1
    if day == n:
        res += 1
        return
    # n의 크기가 8 이하기이기 떄문에 완전탐색으로 해도 무관
    # 방문하지 않은 곳 계산하여 함수 재귀 호출하고
    # 다른 값도 비교하기 위해 백트래킹
    for i in range(n):
        if not visited[i]:
            weight -= k
            weight += a[i]
            visited[i] = 1
            f(day+1, weight)
            weight += k
            weight -= a[i]
            visited[i] = 0


n, k = map(int, input().split())
a = list(map(int, input().split()))
visited = [0] * n
res = 0

for i in range(n):
    # 1일차를 먼저 계산하고 함수 호출
    visited[i] = 1
    weight = 500
    weight -= k
    weight += a[i]
    f(1, weight)
    visited[i] = 0

print(res)