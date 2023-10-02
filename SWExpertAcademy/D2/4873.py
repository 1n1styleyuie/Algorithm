# 테스트 케이스 입력
T = int(input())
for tc in range(1, T+1):
    # 문자열 입력
    str1 = input()
    # 스택 생성
    stack = []
    for i in str1:
        # 먼저 스택에 추가
        stack.append(i)
        # i가 추가된 스택의 길이가 1 이하이면 비교할 대상이 없기 때문에 continue
        if len(stack) <= 1:
            continue
        else:
            # 만약 가장 끝과 그 전에 있는 값이 같다면
            if stack[-1] == stack[-2]:
                # 그 둘 모두 pop
                stack.pop()
                stack.pop()
    print(f'#{tc} {len(stack)}')