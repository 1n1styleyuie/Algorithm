# 14729 s5
import sys
input = sys.stdin.readline


n = int(input())
arr = [float(input()) for _ in range(n)]
arr.sort()

for i in range(7):
    print(f'{arr[i]:.3f}')