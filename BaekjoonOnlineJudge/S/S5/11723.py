# 11723 s5
import sys
input = sys.stdin.readline

m = int(input())
s = set()

for _ in range(m):
    tmp = list(input().rstrip().split())

    if len(tmp) == 1:
        if tmp[0] == 'all':
            s = set([i for i in range(1, 21)])
        else:
            s = set()
    else:
        a, b = tmp[0], tmp[1]
        b = int(b)

        if a == 'add':
            s.add(b)
        elif a == 'remove':
            # set에서 remove를 쓰면 set 안에 해당값이 없을 경우 keyerror가 난다.
            # 그걸 방지하기 위해 discard를 사용한다.
            s.discard(b)
        elif a == 'check':
            if b in s:
                print(1)
            else:
                print(0)
        elif a == 'toggle':
            if b in s:
                s.discard(b)
            else:
                s.add(b)