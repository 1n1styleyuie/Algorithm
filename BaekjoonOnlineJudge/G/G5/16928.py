# 1347 s2
import sys
input = sys.stdin.readline
from collections import deque


n, m = map(int, input().split())

board = [0] * 101

visited = [0] * 101

# 뱀과 사다리를 딕셔너리로 저장
ladder = {}
snake = {}

for _ in range(n):
    x, y = map(int, input().split())
    ladder[x] = y

for _ in range(m):
    x, y = map(int, input().split())
    snake[x] = y

q = deque()
q.append(1)

while q:
    x = q.popleft()

    if x == 100:
        print(board[x])
        break

    # 주사위 숫자는 1부터 6
    for i in range(1, 7):
        next = x + i
        # 사다리 게임의 범위를 벗어나지 않고 방문하지 않은 경우
        if next <= 100 and not visited[next]:

            # 뱀이나 사다리를 타는 경우 next 값을 바꿔준다
            if next in ladder.keys():
                next = ladder[next]
            
            if next in snake.keys():
                next = snake[next]

            if not visited[next]:
                visited[next] = 1
                board[next] = board[x] + 1
                q.append(next)