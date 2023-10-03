import sys

input = sys.stdin.readline


def dfs(x, y):
    stack = []
    stack.append((x, y))

    while stack:
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < h and 0 <= ny < w and arr[nx][ny] == '1':
                stack.append((x, y))
                arr[nx][ny] = '0'
                x = nx
                y = ny
                break
        else:
            x, y = stack.pop()

    return 1


dx = [-1, -1, -1, 0, 0, 1, 1, 1]
dy = [-1, 0, 1, -1, 1, -1, 0, 1]


while True:
    in_, put_ = map(int, input().rstrip().split())
    w, h = in_, put_
    if w == 0 and h == 0:
        break
    arr = [input().rstrip().split() for _ in range(h)]
    ans = 0

    for x in range(h):
        for y in range(w):
            if arr[x][y] == '1':
                ans += dfs(x, y)
                arr[x][y] = '0'

    print(ans)