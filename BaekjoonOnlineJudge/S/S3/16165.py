# 16165 s3
import sys
input = sys.stdin.readline

group = {}
n, m = map(int, input().split())
for _ in range(n):
    name = input().rstrip()
    member = []
    nums = int(input())
    for _ in range(nums):
        member.append(input().rstrip())
    member.sort()
    group[name] = member

for _ in range(m):
    s = input().rstrip()
    q = int(input())
    if q == 0:
        for i in group[s]:
            print(i)
    else:
        for i in group.keys():
            if s in group[i]:
                print(i)