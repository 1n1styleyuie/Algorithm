T = int(input())
for tc in range(1, T+1):
    N = int(input())
    price_lst = list(map(int, input().split()))
    idx = 0
    result = 0

    for i in range(N):
        max_value = price_lst[i]
        if max_value < price_lst[idx] and i < idx:
            max_value = price_lst[idx]
        else:
            for j in range(i, N):
                if max_value < price_lst[j]:
                    max_value = price_lst[j]
                    idx = j
        result += (max_value - price_lst[i])
    print(f'#{tc} {result}')