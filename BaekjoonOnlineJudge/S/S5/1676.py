# 1676 s5
import sys
input = sys.stdin.readline

# 범위가 500까지이기 떄문에 그냥 계산을 통해서 구하면 된다.
n = int(input())
print(n//5 + n//25 + n//125)