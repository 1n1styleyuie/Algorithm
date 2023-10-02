import sys

for _ in range(9):
    arr = [list(map(int, sys.stdin.readline().split()))]

max_num = max(arr)
max_index = arr.index(max_num)

print(max_num)
print(max_index)
