# 1987 g4
import sys
input = sys.stdin.readline

delta = [[0, 1], [0, -1], [1, 0], [-1, 0]]

def dfs(i, j, cnt):
    global max_cnt, visited, previous
    for di, dj in delta:
        ni, nj = i+di, j+dj
        if 0 <= ni < r and 0 <= nj < c:
            # 방문하지 않은 곳과 이전에 있던 알파벳이 아닌 경우에 탐색
            if not visited[ni][nj] and arr[ni][nj] not in previous:
                visited[ni][nj] = 1
                previous.add(arr[ni][nj])
                # 카운트 비교해서 큰 값을 저장
                max_cnt = max(max_cnt, cnt+1)
                dfs(ni, nj, cnt+1)
                # 백트래킹을 위해 다시 바꿔줌
                visited[ni][nj] = 0
                previous.remove(arr[ni][nj])


r, c = map(int, input().split())
arr = [list(input().rstrip()) for _ in range(r)]
visited = [[0] * c for _ in range(r)]

# 같은 알파벳은 들어가지 않을 것이기 때문에 in 을 사용했을 때 시간복잡도를 위해 set을 사용
previous = set()
previous.add(arr[0][0])
max_cnt = 1

dfs(0, 0, 1)
print(max_cnt)

