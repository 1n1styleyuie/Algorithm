import sys
input = sys.stdin.readline
from collections import deque

n = int(input())
cs = []
for _ in range(n):
    s = deque(input().split())
    cs.append(s)

res = True    

l = deque(input().split())
while l:
    s = l.popleft()
    flg = False
    for i in cs:
        if i[0] == s:
            i.popleft()
            if not i:
                cs.remove(i)
            flg = True
            break
    if not flg:
        res = False
        break
        
if cs or res == False:
    print('Impossible')
else:
    print('Possible')