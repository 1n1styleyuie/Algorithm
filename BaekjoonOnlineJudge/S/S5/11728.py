# 11728 s5
import sys
input = sys.stdin.readline


n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))


# 1번풀이
res = a+b
print(*sorted(res))


# 2번풀이
a_idx = 0
b_idx = 0

res = []
while True:
    if a_idx == n:
        res.append(b[b_idx])
        b_idx += 1
    elif b_idx == m:
        res.append(a[a_idx])
        a_idx += 1
    else:
        if a[a_idx] < b[b_idx]:
            res.append(a[a_idx])
            a_idx += 1
        else:
            res.append(b[b_idx])
            b_idx += 1

    if a_idx == n and b_idx == m:
        break

print(*res)
