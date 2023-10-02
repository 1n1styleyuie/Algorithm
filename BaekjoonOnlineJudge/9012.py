T = int(input())
for tc in range(T):
    PS = input()
    stack = [] # 스택 리스트 생성
    for i in PS:
        if i == '(': # 만약 '(' 이 입력될 경우
            stack.append(i) # stack에 추가
        elif i == ')': # 만약 ')' 이 입력될 경우
            # 스택이 0이라면 처음 들어온 값이 ')'이기 때문에 NO로 출력을 해야한다.
            if len(stack) == 0: # 만약 stack의 길이가 0일 경우
                stack.append(i) # stack에 추가
                break # 반복문을 나감
            else:
                stack.pop() # 스택에 있는 값을 pop
    if len(stack) != 0: # stack의 길이가 0이 아니라면
        print('NO')
    else: # 길이가 0이라면
        print('YES')