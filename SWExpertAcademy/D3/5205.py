def partition(arr, left, right):
    p = arr[left]
    i = left
    j = right
    while i <= j:
        while i <= j and arr[i] <= p:
            i += 1
        while i <= j and arr[j] >= p:
            j -= 1
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]
    arr[left], arr[j] = arr[j], arr[left]
    return j


def quick_sort(arr, left, right):
    if left < right:
        s = partition(arr, left, right)
        quick_sort(arr, left, s-1)
        quick_sort(arr, s+1, right)


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    quick_sort(arr, 0, len(arr) - 1)
    print(f'#{tc} {arr[N//2]}')
