while True:
    arr = input()
    if len(arr) == 1 and arr[0] == '.':
        break
    stack = []
    for x in arr:
        if x == '(' or x == '[':
            stack.append(x)
        elif x == ')' or x == ']':
            if not stack:
                stack.append(x)
                break
            elif x == ')':
                if stack[-1] == '(':
                    stack.pop()
                else:
                    break
            elif x == ']':
                if stack[-1] == '[':
                    stack.pop()
                else:
                    break
        else:
            continue
    if stack:
        print('no')
    else:
        print('yes')