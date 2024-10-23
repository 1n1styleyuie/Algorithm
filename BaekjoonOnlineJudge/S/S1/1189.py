# 1189 s1
import sys
input = sys.stdin.readline

delta = [[0, 1], [0, -1], [1, 0], [-1, 0]]


def dfs(cnt, i, j):
    global res
    # 집에 도착했을 때 cnt가 k일 경우에만 +1하여 저장하고 return
    if i == 0 and j == c-1:
        if cnt == k:
            res += 1
        return
    
    for di, dj in delta:
        ni, nj = i+di, j+dj
        if 0 <= ni < r and 0 <= nj < c:
            # T 인 위치가 아닌 곳이며 방문하지 않은 곳을 방문하여
            # dfs함수 호출후 백트래킹을 위해 방문한 곳을 다시 0으로 저장
            if arr[ni][nj] != 'T' and not visited[ni][nj]:
                visited[ni][nj] = 1
                dfs(cnt+1, ni, nj)
                visited[ni][nj] = 0



r, c, k = map(int, input().split())
arr = [list(input().rstrip()) for _ in range(r)]
res = 0
visited = [[0] * c for _ in range(r)]

# 시작 위치부터 카운트하기 때문에 cnt값을 1로 시작하고 현 위치 방문처리
visited[r-1][0] = 1
dfs(1, r-1, 0)

print(res)