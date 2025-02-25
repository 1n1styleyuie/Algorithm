# 27922 s3
import sys
input = sys.stdin.readline


n, k = map(int, input().split())
ab = []
bc = []
ac = []

for _ in range(n):
    a, b, c = map(int, input().split())
    ab.append(a+b)
    bc.append(b+c)
    ac.append(a+c)

ab.sort(reverse=True)
bc.sort(reverse=True)
ac.sort(reverse=True)

sab = sum(ab[:k])
sbc = sum(bc[:k])
sac = sum(ac[:k])

print(max(sab, sbc, sac))