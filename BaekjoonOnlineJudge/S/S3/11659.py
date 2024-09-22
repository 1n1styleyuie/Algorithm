# 11659 s3
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = list(map(int, input().split()))

# 구간 합 중 처음은 아무것도 더해지지 않은 상태를 total에 저장하고 시작한다.
total = [0]


tmp = 0
for a in arr:
    tmp += a
    total.append(tmp)


for _ in range(m):
    i, j = map(int, input().split())
    print(total[j] - total[i-1])