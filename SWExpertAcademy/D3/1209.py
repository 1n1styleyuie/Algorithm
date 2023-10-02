import sys
sys.stdin = open('input.txt', 'r')

for _ in range(10):
    T = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]

    max_1 = 0
    for i in range(100):
        result1 = 0
        for j in range(100):
            result1 += arr[i][j]
        if max_1 < result1:
            max_1 = result1

    max_2 = 0
    for i in range(100):
        result2 = 0
        for j in range(100):
            result2 += arr[j][i]
        if max_2 < result2:
            max_2 = result2

    max_3 = 0
    for i in range(100):
        sum1 = 0
        sum2 = 0
        sum1 += arr[i][i]
        sum2 += arr[i][99-i]

    if max(sum1, sum2) > max_3:
        max_3 = max(max_1, max_2)

    print(f'#{T} {max(max_1, max_2, max_3)}')