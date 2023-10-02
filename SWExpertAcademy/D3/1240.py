T = int(input())
for tc in range(1, T + 1):
    n, m = map(int, input().split())
    arr = [list(map(int, input())) for _ in range(n)]
    scanner = {'0001101': 0, '0011001': 1, '0010011': 2, '0111101': 3,
               '0100011': 4, '0110001': 5, '0101111': 6, '0111011': 7,
               '0110111': 8, '0001011': 9}
    str1 = ''
    for i in range(n - 1, -1, -1):
        for j in range(m - 1, -1, -1):
            if arr[i][j] == 1:
                x = i
                y = j
                break

    for k in range(y, y - 56, -7):
        str2 = ''
        for l in range(k, k - 7, -1):
            str2 = str(arr[x][l]) + str2
        str1 += str(scanner[str2])
    odds = 0
    even = 0
    for s in range(len(str1)):
        if s % 2 == 0:
            even += int(str1[s])
        else:
            odds += int(str1[s])

    code_num = even + odds * 3
    res = odds + even
    if code_num % 10 == 0:
        print(f'#{tc} {res}')
    else:
        print(f'#{tc} 0')