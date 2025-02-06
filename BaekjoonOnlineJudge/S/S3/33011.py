# 29812 s5
import sys
input = sys.stdin.readline


t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))

    n1, n2 = 0, 0
    for a in arr:
        if a % 2 == 1:
            n1 += 1
        else:
            n2 += 1
    
    if n1 < n2:
        tmp = n1
        n1 = n2
        n2 = tmp
    
    if n1 % 2 == 1 and n1 != n2:
        print('amsminn')
    else:
        print('heeda0528')