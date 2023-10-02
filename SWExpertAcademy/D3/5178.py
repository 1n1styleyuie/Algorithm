T = int(input())
for tc in range(1, T + 1):
    N, M, L = map(int, input().split())
    arr = [0] * (N + 1)
    for leaf in range(M):
        node, value = map(int, input().split())
        arr[node] = value

    for i in range(N, 0, -1):
        sum_num = arr[i]
        arr[i // 2] += sum_num

    print(f'#{tc} {arr[L]}')  