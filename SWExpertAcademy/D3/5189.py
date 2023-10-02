def f(start, total):
    global result

    if sum(visited) == N:
        total += arr[start][0]
        if result > total:
            result = total
        return

    for i in range(N):
        if not visited[i]:
            visited[i] = 1
            f(i, total+arr[start][i])
            visited[i] = 0


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    visited = [0] * N
    result = 1e9
    visited[0] = 1
    f(0, 0)

    print(f'#{tc} {result}')