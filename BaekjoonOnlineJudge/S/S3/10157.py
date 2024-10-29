# 10157 s3
import sys
input = sys.stdin.readline

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def f(x, y):
    tmp = 1
    i = 0
    while True:
        if tmp == k:
            return x + 1, y + 1
        # y와 x의 위치가 다른 문제들과 다르다는것에 유의
        visited[y][x] = 1
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < c and 0 <= ny < r:
            if not visited[ny][nx]:
                x, y = nx, ny
                tmp += 1
            else:
                i = (i + 1) % 4
        else:
            i = (i + 1) % 4


c, r = map(int, input().split())
k = int(input())
visited = [[0] * (c+1) for _ in range(r+1)]

if k > c * r:
    print(0)
else:
    print(*f(0, 0))