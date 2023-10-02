icp = {'(': 3, '*': 2, '/': 2, '+': 1, '-': 1}
isp = {'(': 0, '*': 2, '/': 2, '+': 1, '-': 1}


def f(susik):
    return_str = ''
    stack = []*100
    for x in susik:
        if x == ')':                   # 토큰이 ')'라면
            while stack[-1] != '(':         # 스택의 탑이 '('가 올 때까지
                return_str += stack.pop()   # 스택의 탑을 출력
            stack.pop()                     # '('는 출력안하고 pop만
        elif x in '+-*/(':             # 토큰이 연산자이면,
            if stack:                       # 스택에 뭔가 들어있다면
                if icp[x] > isp[stack[-1]]:
                    stack.append(x)
                else:
                    while True:
                        return_str += stack.pop()
                        if not stack:
                            stack.append(x)
                            break
                        elif icp[x] > isp[stack[-1]]:
                            stack.append(x)
                            break
            else:                           # 스택이 비어있다면
                stack.append(x)    # 스택에 연산자 추가
        else:
            return_str += x
    while stack:
        return_str += stack.pop()
    return return_str

sentence = input()
print(f(sentence))