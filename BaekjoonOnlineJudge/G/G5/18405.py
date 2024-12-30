# 18405 g5
import sys
input = sys.stdin.readline
from collections import deque


delta = [[0, 1], [0, -1], [1, 0], [-1, 0]]
n, k = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
s, x, y = map(int, input().split())

virus = []
for t in range(1, k+1):
    for a in range(n):
        for b in range(n):
            if arr[a][b] == t:
                virus.append((t, a, b))


virus.sort()
q = deque(virus)
time = 0
while q:
    if time == s:
        break
    for _ in range(len(q)):
        m, i, j = q.popleft()
        for di, dj in delta:
            ni, nj = i + di, j + dj
            if 0 <= ni < n and 0 <= nj < n:
                if arr[ni][nj] == 0:
                    arr[ni][nj] = m
                    q.append((m, ni, nj))
    time += 1

print(arr[x-1][y-1])