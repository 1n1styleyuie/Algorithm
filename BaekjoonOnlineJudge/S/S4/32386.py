# 32386 s4
import sys
input = sys.stdin.readline


n = int(input())
tag = {}
for _ in range(n):
    lst = input().rstrip().split()
    s = int(lst[0])
    t = int(lst[1])
    arr = lst[2:]
    for a in arr:
        if a not in tag:
            tag[a] = 1
        else:
            tag[a] += 1

tags = sorted(tag.items(), key= lambda x : -x[1])

if len(tags) == 1:
    print(tags[0][0])
else:
    if tags[0][1] == tags[1][1]:
        print(-1)
    else:
        print(tags[0][0])