def inorder(n):
    if n <= N:
        inorder(n * 2)
        print(arr[n], end='')
        inorder(n * 2 + 1)


T = 10
for tc in range(1, T + 1):
    N = int(input())
    arr = [0] * (N + 1)
    for i in range(N):
        str_lst = list(input().split())
        arr[i + 1] = str_lst[1]
    print(f'#{tc}', end=' ')
    inorder(1)
    print()