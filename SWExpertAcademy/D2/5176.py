def inorder(n):
    global number
    if n <= N:
        inorder(n * 2)
        arr[n] = number
        number += 1
        inorder(n * 2 + 1)


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [0] * (N+1)
    number = 1
    inorder(1)

    print(f'#{tc} {arr[1]} {arr[N // 2]}')