# 10867 s5
import sys
input = sys.stdin.readline


n = int(input())
arr = set(map(int, input().split()))
print(*sorted(arr))