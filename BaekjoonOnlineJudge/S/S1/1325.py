# 1325 s1
import sys
input = sys.stdin.readline
from collections import deque


def bfs(i):
    q = deque()
    q.append(i)
    visited = [0] * (n+1)
    visited[i] = 1
    cnt = 0
    while q:
        x = q.popleft()
        for a in arr[x]:
            if not visited[a]:
                q.append(a)
                visited[a] = 1
                cnt += 1
    return cnt


n, m = map(int, input().split())
arr = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    arr[b].append(a)

res = []
max_cnt = 0
for i in range(1, n+1):
    c = bfs(i)
    # c가 현재까지 가장 멀리 갈 수 있는 범위보다 크다면 리스트 초기화 후 저장
    if max_cnt < c:
        max_cnt = c
        res.clear()
        res.append(i)
    # 멀리 갈 수 있는 범위가 같으면 리스트에 추가가
    elif max_cnt == c:
        res.append(i)

print(*res)