# 11286 s1
import sys
input = sys.stdin.readline
import heapq


n = int(input())
arr = []
for _ in range(n):
    x = int(input())

    # heappush 할 때 절대값과 주어진 값을 같이 저장하여 heappop할 때 가장 작은 값이 나오도록 한다.
    if x == 0:
        if arr:
            print(heapq.heappop(arr)[1])
        else:
            print(0)
    else:
        heapq.heappush(arr, (abs(x), x))