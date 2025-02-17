# 25556 g5
import sys
input = sys.stdin.readline


n = int(input())
arr = list(map(int, input().split()))

stack = [[0], [0], [0], [0]]

for i in range(n):
    flg = False
    for j in range(4):
        if stack[j][-1] < arr[i]:
            stack[j].append(arr[i])
            flg = True
            break
    
    if not flg:
        print('NO')
        exit()

print('YES')