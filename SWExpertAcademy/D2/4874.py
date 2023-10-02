T = int(input())
for tc in range(1, T+1):
    # 수식을 입력 받음
    susik = list(input().split())
    # 저장할 스택 생성
    stack = []
    for x in susik:
        # 만약 x 가 '.' 이라면
        if x == '.':
            # 스택의 길이가 1이면 숫자가 남아있는 것으로
            # 스택에 저장된 값을 출력
            if len(stack) ==1:
                print(f'#{tc}', *stack)
                break
            # 오류가 난 것이기 때문에 error 출력
            else:
                print(f'#{tc} error')
                break
        # x가 숫자일 경우 스택에 push
        if x.isnumeric():
            stack.append(int(x))
        # 사칙연산 기호일 경우
        elif x in '+-/*':
            # 스택의 길이가 2 이상일 경우에
            if len(stack) >= 2:
                # 숫자 두개를 모두 팝 하여 연산
                b = stack.pop()
                a = stack.pop()
                # 덧셈 연산 후 스택에 저장
                if x == '+':
                    stack.append(a+b)
                # 뺄셈 연산 후 스택에 저장
                elif x == '-':
                    stack.append(a-b)
                # 나눗셈 연산 후 스택에 저장
                elif x == '/':
                    stack.append(a//b)
                # 곱셈 연산 후 스택에 저장
                elif x == '*':
                    stack.append(a*b)
            # 길이가 2 이상이 아닌 경우 계산할 숫자가 부족하기 때문에
            # 에러가 발생했음을 출력
            else:
                print(f'#{tc} error')
                break