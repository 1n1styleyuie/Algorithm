def solution(s):
    answer = True
    stack = []
    for i in s:
        if i == '(':
            stack.append(i)
        else:
            if not stack:
                answer = False
                break
            else:
                stack.pop()
    if stack:
        answer = False
            
    return answer