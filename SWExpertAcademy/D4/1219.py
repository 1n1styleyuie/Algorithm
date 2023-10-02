import sys
sys.stdin = open('input.txt')


def dfs(n, V, adj_m):
    stack = []
    visited = [0] * (V+1)
    visited[n] = 1
    global res
    while True:
        for w in range(1, V+1):
            if adj_m[n][w] == 1:
                if w == 99:
                    res = 1
                    return res
                if visited[w] == 0:
                    stack.append(n)
                    n = w
                    visited[n] = 1
                    break
        else:
            if stack:
                n = stack.pop()
            else:
                break


for test_case in range(1, 11):
    tc, E = map(int, input().split())
    V = 100
    arr = list(map(int, input().split()))
    adj_m = [[0] * (V+1) for _ in range(V+1)]
    for i in range(E):
        v1, v2 = arr[i*2], arr[i*2+1]
        adj_m[v1][v2] = 1
    res = 0
    dfs(0, V, adj_m)
    print(f'#{tc} {res}')