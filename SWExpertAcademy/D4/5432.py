T = int(input())
for tc in range(1, T+1):
    stick = list(input())
    sticks = 0
    pieces = 0
    for i in range(len(stick)):
        if stick[i] == '(':
            sticks += 1
        else:
            sticks -= 1
            if stick[i-1] == '(':
                pieces += sticks
            else:
                pieces += 1
    print(f'#{tc} {pieces}')
