T = int(input())
for tc in range(1, T+1):
    arr = [list(input()) for _ in range(5)]
    stack = []
    for j in range(15):
        for i in range(5):
            try:
                stack.append(arr[i][j])
            except:
                continue
    print(f'#{tc}', ''.join(stack))