T = int(input())
for tc in range(1, T+1):
    N = float(input())
    res = ''
    while N < 1:
        N *= 2
        if N == 1:
            res += '1'
            break
        elif N > 1:
            N -= 1
            res += '1'
        else:
            res += '0'

    if len(res) > 12:
        print(f'#{tc} overflow')
    else:
        print(f'#{tc} {res}')