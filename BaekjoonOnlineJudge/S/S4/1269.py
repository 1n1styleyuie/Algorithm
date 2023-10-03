import sys

N, M = map(int, sys.stdin.readline().split())
a_num = list(map(int, sys.stdin.readline().split()))
b_num = list(map(int, sys.stdin.readline().split()))


complement1 = list(set(a_num) - set(b_num))
complement2 = list(set(b_num) - set(a_num))


print(len(complement1) + len(complement2))