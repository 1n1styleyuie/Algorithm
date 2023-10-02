def binarySearch(N, key):
    start = 1
    end = N
    count = 0
    while start <= end:
        middle = int((start+end) / 2)
        if middle == key:
            return count
        elif middle > key:
            count += 1
            end = middle
        else:
            count += 1
            start = middle

T = int(input())

for tc in range(1, T+1):
    N, Pa, Pb = map(int, input().split())
    count_a = binarySearch(N, Pa)
    count_b = binarySearch(N, Pb)
    if count_a > count_b:
        print(f'#{tc} B')
    elif count_a < count_b:
        print(f'#{tc} A')
    else:
        print(f'#{tc} 0')