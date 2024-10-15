# 1927 s2
import sys
input = sys.stdin.readline

import heapq

n = int(input())

min_heap = []
for _ in range(n):
    x = int(input())
    # x가 0일 때 배열에 값이 없을 경우 0을 출력
    # x가 0일 때 배열에서 가장 작은 값을 출력하고 제거
    if x == 0:
        if not min_heap:
            print(0)
        else:
            print(heapq.heappop(min_heap))
    # 그 외 경우 배열에 값을 추가
    else:
        heapq.heappush(min_heap, x)
