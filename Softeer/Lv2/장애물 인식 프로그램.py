import sys
from collections import deque

input = sys.stdin.readline
delta = [[0, 1], [0, -1], [1, 0], [-1, 0]]

def bfs(x,y):
    global cnt
    q = deque()
    q.append((x, y))
    while q:
        i, j = q.popleft()
        for di, dj in delta:
            ni, nj = i+di, j+dj
            if 0 <= ni < N and 0 <= nj < N:
                if arr[ni][nj] == 1:
                    arr[ni][nj] = 0
                    q.append((ni, nj))
                    cnt += 1



N = int(input())

arr = [list(map(int, input().rstrip())) for _ in range(N)]

answer = []



for i in range(N):
    for j in range(N):
        if arr[i][j] == 1:
            arr[i][j] = 0
            cnt = 1
            bfs(i, j)
            answer.append(cnt)


answer.sort()
print(len(answer))
print(*answer, sep='\n')