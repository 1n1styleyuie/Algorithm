# 23561 s2
import sys
input = sys.stdin.readline


n = int(input())
arr = list(map(int, input().split()))
arr.sort()
print(abs(arr[n] - arr[n + n - 1]))