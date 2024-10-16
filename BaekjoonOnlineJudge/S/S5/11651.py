# 11651 s5
import sys
input = sys.stdin.readline

n = int(input())
arr = []
for _ in range(n):
    x, y = map(int, input().split())
    arr.append((x, y))
    
arr.sort(key=lambda x: (x[1], x[0]))

for a in arr:
    print(a[0], a[1])