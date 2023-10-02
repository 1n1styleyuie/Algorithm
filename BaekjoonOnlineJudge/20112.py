import sys
input = sys.stdin.readline

N = int(input())
arr = [list(input()) for _ in range(N)]

row = ''
col = ''
for i in range(N):
    for j in range(N):
        row += arr[i][j]
        col += arr[j][i]

if row == col:
    print('YES')
else:
    print('NO')