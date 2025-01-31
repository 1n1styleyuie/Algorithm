# 13414 s3
import sys
input = sys.stdin.readline


k, l = map(int, input().split())
arr = {}
for i in range(l):
    a = input().rstrip()
    arr[a] = i

res = sorted(arr.items(), key=lambda x : x[1])
if k > len(res):
    k = len(res)

for i in range(k):
    number, n = res[i]
    print(number)