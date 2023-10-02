def f(i, N, total):
    global max_percent
    if total <= max_percent:
        return
    if i == N:
        if total > max_percent:
            max_percent = total
        return

    for j in range(N):
        if not visited[j]:
            visited[j] = 1
            f(i + 1, N, total*(arr[i][j]/100))
            visited[j] = 0


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    max_percent = 0
    visited = [0] * N
    f(0, N, 1)
    res = max_percent*100
    print(f'#{tc} {res:6f}')