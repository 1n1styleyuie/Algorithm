# 17413 s3
import sys
input = sys.stdin.readline
from collections import deque

ss = list(input().rstrip())

res = ''
q = deque()
tag = False
for s in ss:
    # s가 < 일 경우 tag를 True로 바꿔줌
    if s == '<':
        q.append(s)
        tag = True
    # s가 > 일 경우 tag를 False로 바꾸고 현재까지 저장된 값들을 res에 저장
    elif s == '>':
        for i in q:
            res += i
        res += s
        q.clear()
        tag = False
    # 공백일 경우 현재까지 q에 저장된 값들을 res로 저장후 q를 clear
    elif s == ' ':
        for i in q:
            res += i
        res += s
        q.clear()
    else:
        # 태그가 True일 경우 태그안에 있는 문자이기 때문에 append
        # 태그가 False일 경우 appendleft를 하여 q의 맨 앞으로 저장
        if tag:
            q.append(s)
        else:
            q.appendleft(s)

# q에 남아있던 단어들을 res에 저장
if q:
    for i in q:
        res += i

print(res)