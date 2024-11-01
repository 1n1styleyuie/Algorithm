# 14503
import sys
input = sys.stdin.readline

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def f(x, y, d):
    global cnt
    while True:
        # 청소가 안된 곳은 청소한 후 -1로 저장
        # 1로 저장하면 벽으로 인식하여 후진이 불가능하기 때문에 -1로 저장함
        if arr[x][y] == 0:
            arr[x][y] = -1
            cnt += 1
        
        for _ in range(4):
            # (d+3) % 4 로 방향을 반시계방향으로 회전시킴
            d = (d+3) % 4
            nx, ny = x + dx[d], y + dy[d]
            # 갈 수 있는 곳이라면 x, y 바꿔주고 break
            if (0<=nx<n and 0<=ny<m) and arr[nx][ny] == 0:
                x, y = nx, ny
                break
        # 4방향 탐색을 했을 때 청소할 곳이 없다면 뒤로 후진하고
        # 만약 후진을 해도 범위를 벗어나거나 벽일 경우 그대로 중단
        else:
            x, y = x+dx[d]*(-1), y+dy[d]*(-1)
            if (0<=x<n and 0<=y<m) and arr[x][y] == 1 or not (0<=x<n and 0<=y<m):
                return 


n, m = map(int, input().split())
r, c, d = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
cnt = 0

f(r, c, d)
print(cnt)