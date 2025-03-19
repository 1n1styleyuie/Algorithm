# 31869 s3
import sys
input = sys.stdin.readline


n = int(input())
res = 0
arr = {}
for _ in range(n):
    s, w, d, p = input().rstrip().split()
    arr[s] = [(int(w)-1)*7 + int(d), int(p)]


date = [0] * 70


for _ in range(n):
    name, money = input().rstrip().split()
    if int(money) - arr[name][1] >= 0:
        date[arr[name][0]] = 1
    
res = 0
cnt = 0
for d in date:
    if d:
        cnt += 1
    else:
        res = max(cnt, res)
        cnt = 0
    
res = max(cnt, res)
print(res)

