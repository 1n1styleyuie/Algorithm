# 25955 s4
import sys
input = sys.stdin.readline


n = int(input())
arr = input().rstrip().split()
level = {'B' : 1, 'S' : 2, 'G' : 3, 'P' : 4, 'D' : 5}

sort_arr = sorted(arr, key=lambda x : (level[x[0]], -int(x[1:])))

if arr == sort_arr:
    print('OK')
    exit(0)
else:
    res = []
    for i in range(n):
        if arr[i] != sort_arr[i]:
            res.append(arr[i])
    
    print('KO')
    print(*sorted(res, key=lambda x : (level[x[0]], -int(x[1:]))))