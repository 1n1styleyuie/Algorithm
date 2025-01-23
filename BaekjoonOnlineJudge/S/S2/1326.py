# 1326 s2
import sys
input = sys.stdin.readline
from collections import deque


def bfs():
    q = deque()
    q.append(a-1)
    visited = [0] * n
    visited[a-1] = 1

    while q:
        x = q.popleft()

        for i in range(x, n, arr[x]):
            if not visited[i]:
                q.append(i)
                visited[i] = visited[x] + 1

                if i == b-1:
                    return visited[i]-1
        
        for i in range(x, -1, -arr[x]):
            if not visited[i]:
                q.append(i)
                visited[i] = visited[x] + 1

                if i == b-1:
                    return visited[i]-1

    return -1


n = int(input())
arr = list(map(int, input().split()))
a, b = map(int, input().split())
print(bfs())