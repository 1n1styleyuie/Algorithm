# 14425 s4
import sys
input = sys.stdin.readline


# 시간초과를 막기 위해 set을 사용하여 in 내장함수 사용
n, m = map(int, input().split())
arr = set()
for _ in range(n):
    arr.add(input().rstrip())

cnt = 0
for _ in range(m):
    s = input().rstrip()
    if s in arr:
        cnt += 1

print(cnt)