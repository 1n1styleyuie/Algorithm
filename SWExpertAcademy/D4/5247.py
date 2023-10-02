from collections import deque

def f(n, m):
    q = deque()
    q.append((n, 0)) # 시작점, 카운트
    visited = [0] * 1000001 # 방문 기록
    while q:
        x, cnt = q.popleft()
        # 도달했으면 return
        if x == m:
            return cnt
        # +1 연산
        if 1<=x+1<=1000000 and not visited[x+1]:
            q.append((x + 1, cnt + 1))
            visited[x + 1] = 1
        # -1 연산
        if 1<=x-1<=1000000 and not visited[x - 1]:
            q.append((x - 1, cnt + 1))
            visited[x - 1] = 1
        # *2 연산
        if 1<=x*2<=1000000 and not visited[x * 2]:
            q.append((x * 2, cnt + 1))
            visited[x * 2] = 1
        # -10 연산
        if 1<=x-10<=1000000 and not visited[x - 10]:
            q.append((x - 10, cnt + 1))
            visited[x - 10] = 1


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    res = f(N, M)
    print(f'#{tc} {res}')