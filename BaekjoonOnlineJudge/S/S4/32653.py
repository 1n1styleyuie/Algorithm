# 32653 s4
import sys
input = sys.stdin.readline
import math


n = int(input())
arr = list(map(int, input().split()))
lst = []
for a in arr:
    lst.append(a*2)
print(math.lcm(*lst))