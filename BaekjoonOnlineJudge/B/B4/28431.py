# 28431
arr = set()
res = 0
for _ in range(5):
    n = int(input())
    if n in arr:
        res -= n
        arr.discard(n)
    else:
        arr.add(n)
        res += n
print(res)