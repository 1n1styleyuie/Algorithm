# 18870
import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
arrset = set(arr)
a = list(arrset)
a.sort()

numdic = {}
for i in range(len(a)):
    numdic[a[i]] = i

for i in arr:
    print(numdic[i], end=' ')