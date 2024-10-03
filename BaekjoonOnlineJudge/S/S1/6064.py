# 6064 s1
import sys
input = sys.stdin.readline

def f(m, n, x, y):
    k = x
    # 최대 범위는 m * n
    while k <= m * n:
        # 나눴을 때 나머지가 0이 되는 지점이 x, y의 해이다.
        if (k - x) % m == 0 and (k - y) % n == 0:
            return k
        # k - x 는 m의 배수이기 떄문에 m만 더해준다.
        k += m 
    return -1

t = int(input())
for _ in range(t):
    m, n, x, y = map(int, input().split())
    print(f(m, n, x, y))
