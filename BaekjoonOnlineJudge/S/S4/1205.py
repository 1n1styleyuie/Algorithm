# 1205 s4
import sys
input = sys.stdin.readline

n, new, p = map(int, input().split())
if n == 0:
    arr = []
else:
    arr = list(map(int, input().split()))

arr.sort(reverse=True)

rank = 1
cnt = 0
for a in arr:
    # 새로운 점수보다 큰 경우는 rank를 +1
    if a > new:
        rank += 1
    # 동일 점수일 경우 카운트에 +1
    elif a == new:
        cnt += 1

# rank와 cnt의 합이 p보다 넘는 경우 -1 출력
if rank + cnt > p:
    print(-1)
else:
    print(rank)