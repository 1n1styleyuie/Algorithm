def selectionSort(a, N):
    for i in range(N-1):
        min_Idx = i
        for j in range(i+1, N):
            if a[min_Idx] > a[j]:
                min_Idx = j
        a[i], a[min_Idx] = a[min_Idx], a[i]
    return a


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    result = selectionSort(arr, N)
    result_list = []
    for i in range(5):
        result_list.append(result[N-i-1])
        result_list.append(result[i])
    print(f'#{tc}', *result_list)
