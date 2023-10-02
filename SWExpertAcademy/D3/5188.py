def f(i, j, N, total):
    global result
    if i == N-1 and j == N-1:
        if result > total:
            result = total
        return
    else:
        for di, dj in [[0, 1], [1, 0]]:
            ni, nj = i+di, j+dj
            if 0 <= ni < N and 0 <= nj < N:
                if total <= result:
                    f(ni, nj, N, total + arr[ni][nj])


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    result = 1e9
    total = arr[0][0]
    f(0, 0, N, total)
    print(f'#{tc} {result}')
