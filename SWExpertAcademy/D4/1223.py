import sys
sys.stdin = open('input.txt')

# *가 먼저 계산되도록 우선순위 설정
def priority(char):
    if char == '*':
        return 3
    elif char == '+':
        return 2
    else:
        return 1

# 중위표기 > 후위표기
def to_postfix():
    stack1 = []
    stack2 = []
    for i in range(n):
        num = priority(arr[i])
        if num == 3:
            while stack1:
                if priority(stack1[-1]) < num:
                    break
                stack2.append(stack1.pop())
            stack1.append(arr[i])
        elif num == 2:
            while stack1:
                if priority(stack1[-1]) < num:
                    break
                stack2.append(stack1.pop())
            stack1.append(arr[i])
        else:
            stack2.append(int(arr[i]))
    while stack1:
        stack2.append(stack1.pop())
    return stack2

# 계산
def calculate(arr):
    stack = []
    for i in range(n):
        if arr[i] == '+':
            B = stack.pop()
            A = stack.pop()
            stack.append(A + B)
        elif arr[i] == '*':
            B = stack.pop()
            A = stack.pop()
            stack.append(A * B)
        else:
            stack.append(arr[i])
    return stack


for test_case in range(1, 11):
    n = int(input())
    arr = input()
    print(f'#{test_case}', *calculate(to_postfix()))
