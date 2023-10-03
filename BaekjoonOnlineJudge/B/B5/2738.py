import sys
N, M = map(int, sys.stdin.readline().split())
list1 = []
list2 = []

for i in N:
    for j in M:
        list1[i][j] = map(int, sys.stdin.readline().split())

print(list1)