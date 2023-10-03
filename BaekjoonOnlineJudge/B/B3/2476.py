# 2476
n = int(input())
res = 0
for _ in range(n):
    a, b, c = map(int, input().split())
    if a == b and b == c and a == c:
        res = max(res, 10000 + a * 1000)
    elif a == b:
        res = max(res, 1000 + a * 100)
    elif a == c:
        res = max(res, 1000 + a * 100)
    elif c == b:
        res = max(res, 1000 + b * 100)
    elif a != b and b != c and a != c:
        res = max(res, max(a, b, c) * 100)
print(res)