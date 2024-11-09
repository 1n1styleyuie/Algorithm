# 14500 g4
import sys
input = sys.stdin.readline

delta = [[0, 1], [0, -1], [1, 0], [-1, 0]]


# 백트래킹 형식으로 4개를 이어 붙였을 경우의 최대값을 찾기
def back(i, j, cnt, total):
    global max_total

    if cnt == 4:
        max_total = max(max_total, total)
        return

    for di, dj in delta:
        ni, nj = i+di, j+dj
        if 0<=ni<n and 0<=nj<m:
            if not visited[ni][nj]:
                visited[ni][nj] = 1
                back(ni, nj, cnt+1, total+arr[ni][nj])
                visited[ni][nj] = 0


# 테트로미노에서 한변씩만 붙어있는 도형이 아닌 두개의 변이 붙어있는 도형이 딱 하나 있다.
# 해당 도형만 따로 값을 계산하여 최대값을 찾기
def f(x, y):
    global max_total
    block = [[[-1, 1], [0, 1], [1, 1]],
            [[1, -1], [1, 0], [1, 1]],
            [[1, -1], [0, -1], [-1, -1]],
            [[-1, -1], [-1, 0], [-1, 1]]]
    
    for i in range(4):
        total = arr[x][y]
        x1, y1, x2, y2, x3, y3 = x+block[i][0][0], y+block[i][0][1], x+block[i][1][0], y+block[i][1][1], x+block[i][2][0], y+block[i][2][1]
        if 0<=x1<n and 0<=x2<n and 0<=x3<n and 0<=y1<m and 0<=y2<m and 0<=y3<m:
            if not visited[x1][y1] and not visited[x2][y2] and not visited[x3][y3]:
                total += arr[x1][y1] + arr[x2][y2] + arr[x3][y3]
                max_total = max(max_total, total)


n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
visited = [[0] * m for _ in range(n)]
max_total = 0

for i in range(n):
    for j in range(m):
        visited[i][j] = 1
        back(i, j, 1, arr[i][j])
        f(i, j)
        visited[i][j] = 0

print(max_total)