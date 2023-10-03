import sys

N = int(sys.stdin.readline())
num1_list = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
num2_list = list(map(int, sys.stdin.readline().split()))
res_list  = {}


for i in num1_list:
    if i in res_list:
        res_list[i] += 1
    else:
        res_list[i] = 1

print(' '.join(str(res_list[m])if m in res_list else '0' for m in num2_list))


  