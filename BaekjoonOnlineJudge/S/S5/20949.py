# 20949 s5
import sys
input = sys.stdin.readline


n = int(input())
arr = []
for i in range(1, n+1):
    w, h = map(int, input().split())
    ppi = (((w ** 2) + (h ** 2)) ** (1/2)) / 77
    arr.append((i, ppi))

arr.sort(key= lambda x : -x[1])

for j in range(n):
    print(arr[j][0])