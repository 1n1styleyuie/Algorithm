# 1874 s2
import sys
input = sys.stdin.readline

n = int(input())
stack = []
res = []
idx = 1
flg = True
for _ in range(n):
    num = int(input())
    # idx가 num값과 같아질때 까지 stack에 추가
    while idx <= num:
        stack.append(idx)
        res.append('+')
        idx += 1
    # stack의 최상단에 있는 값이 num과 같으면 pop
    if stack[-1] == num:
        stack.pop()
        res.append('-')
    # 같지 않으면 만들어질수 없는 수열이다.
    else:
        flg = False
if flg:
    for i in range(len(res)):
        print(res[i])
else:
    print('NO')
