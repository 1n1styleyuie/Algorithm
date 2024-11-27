# 1389 s1
import sys
input = sys.stdin.readline
from collections import deque


def bfs(start):
    q = deque()
    q.append(start)
    visited[start] = 1
    # 케빈 베이컨 수를 저장할 배열 생성
    num = [0] * (n+1)
    while q:
        x = q.popleft()
        for i in arr[x]:
            # 방문하지 않은 곳을 방문 한 뒤 케빈베이컨 수를 저장
            if not visited[i]:
                num[i] = num[x] + 1
                visited[i] = 1
                q.append(i)
    
    return sum(num)


n, m = map(int, input().split())
arr = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)

res = []
for i in range(1, n+1):
    # 방문 확인용 배열 생성
    visited = [0] * (n+1)
    res.append(bfs(i))


print(res.index(min(res))+1)