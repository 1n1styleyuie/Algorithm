# 1074 g5
import sys
input = sys.stdin.readline

n, r, c = map(int, input().split())

res = 0


while n > 0:
    
    n -= 1
    # 제2사분면
    if r < 2 ** n and c < 2 ** n:
        res += (2 ** n) * (2 ** n) * 0
    # 제1사분면
    elif r < 2 ** n and c >= 2 ** n:
        res += (2 ** n) * (2 ** n) * 1
        c -= (2 ** n)
    # 제3사분면
    elif r >= 2 ** n and c < 2 ** n:
        res += (2 ** n) * (2 ** n) * 2
        r -= (2 ** n)
    # 제4사분면
    else:
        res += (2 ** n) * (2 ** n) * 3
        r -= (2 ** n)
        c -= (2 ** n)

print(res)