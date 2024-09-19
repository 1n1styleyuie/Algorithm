# 15565 s1
import sys
input = sys.stdin.readline

n, k = map(int, input().split())
arr = list(map(int, input().split()))


idx = []
# 라이언 인형 위치를 idx에 저장
for i in range(n):
    if arr[i] == 1:
        idx.append(i)


res = 10**8
# idx에서 연속된 k개만큼 선택했을 때 가장 짧은 길이를 res에 저장
for i in range(len(idx)-k+1):
    res = min(res, idx[i+k-1]-idx[i]+1)


if res == 10**8:
    print(-1)
else:
    print(res)