# 9935 g4
import sys
input = sys.stdin.readline

ss = input().rstrip()
bomb = input().rstrip()

# 시간 초과 코드
# while bomb in ss:
#     ss = ss.replace(bomb, '')

# if ss:
#     print(ss)
# else:
#     print('FRULA')

'''
stack에 문자를 하나씩 저장하면서
stack의 뒤에서부터 폭발문자열의 길이만큼 문자열을 만들었을 때 폭발문자열과 같다면 길이만큼 pop하여 빼준다.

ex)
mirkovC4nizCC44
C4

mirkovC4까지 stack에 append된 후 뒤에서부터 폭발 문자열의 길이만큼 자르면 C4이고 폭발 문자열과 같기 때문에 길이만큼 pop한다.
stack에는 mirkov 가 남는다.
nizCC4 까지 append된 후 stack은 mirkovnizCC4가 남는다. 폭발 문자열 길이만큼 잘랐을 경우 폭발 문자열과 같기 때문에 pop한다.
stack에는 mirkovnizC 가 남는다.
4 append 후 stack에는 mirkovnizC4가 남고 C4를 pop하여주고 print하면 된다.

12ab112ab2ab
12ab

12ab 까지 append 후 pop한다. stack은 빈 리스트이다.
112ab 까지 append 후 pop한다. stack에는 1 만 남는다.
2ab 까지 append 후 stack엔 12ab가 남는다. 폭발 문자열인지 확인 후 pop한다. stack에는 아무것도 남지 않기 때문에 FRULA를 출력한다.
'''

stack = []
for s in ss:
    stack.append(s)
    if ''.join(stack[-(len(bomb)):]) == bomb:
        for _ in range(len(bomb)):
            stack.pop()

if stack:
    print(''.join(stack))
else:
    print('FRULA')