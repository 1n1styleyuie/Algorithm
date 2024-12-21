# 10799 s2
import sys
input = sys.stdin.readline


s = input().rstrip()
stack = []
res = 0

for idx in range(len(s)):
    if s[idx] == '(':
        stack.append(s[idx])
    else:
        stack.pop()
        # 이전위치가 ( 일 경우 stack에 있는 길이만큼 자르고
        # 이전 위치가 ( 가 아닐 경우엔 마지막 위치이기 때문에 +1 한다
        if s[idx-1] == '(':
            res += len(stack)
        else:
            res += 1

print(res)