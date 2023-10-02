T = int(input())
for tc in range(1, T+1):
    word = input().strip()
    stack = []
    for i in word:
        # 만약 ( 혹은 { 라면 stack에 추가
        if i == '(' or i == '{':
            stack.append(i)
        # 만약 ) 혹은 } 라면
        elif i == ')' or i == '}':
            # stack에 아무것도 존재하지 않는다면 추가 한후 반복문 정지
            if not stack:
                stack.append(i)
                break
            # i가 )일때 peek가 (이 아니라면, i가 }일 때 peek가 {이 아니라면
            elif (i == ')' and stack[-1] != '(') or (i == '}' and stack[-1] != '{'):
                # stack에 추가 후 반복문 정지
                stack.append(i)
                break
            else:
                # 그 외의 경우에는 정상적으로 짝이 맞기 때문에 pop
                stack.pop()
    # 길이가 0이 아닌것은 정상적으로 짝이 맞지 않았다는 것이기 때문에 0 출력
    if len(stack) != 0:
        print(f'#{tc} 0')
    else:
        print(f'#{tc} 1')