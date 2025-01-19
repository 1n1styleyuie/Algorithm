# 19583 s2
import sys
input = sys.stdin.readline


s, e, q = input().rstrip().split()

s = int(s[:2] + s[3:])
e = int(e[:2] + e[3:])
q = int(q[:2] + q[3:])


member = set()
res = 0

while True:
    l = input().rstrip()
    if len(l) < 5:
        break

    t, name = l.split()
    time = int(t[:2] + t[3:])
    if time <= s:
        member.add(name)
    elif e <= time <= q:
        if name in member:
            member.remove(name)
            res += 1

print(res)