# 14889 s1
import sys
input = sys.stdin.readline

# cnt는 현재까지 몇번 탐색했는지 확인하며 n//2만큼 탐색을 완료했다면 결과값을 저장
def back(cnt, idx):
    global ans
    if cnt == n//2:
        start = 0
        link = 0
        # 방문한곳과 방문하지 않은 곳을 나누어 저장 후 최소값을 ans에 저장
        for i in range(n):
            for j in range(n):
                if visited[i] and visited[j]:
                    start += s[i][j]
                elif not visited[i] and not visited[j]:
                    link += s[i][j]
        ans = min(ans, abs(start - link))
        return
    # 다음 인덱스를 백트래킹하면서 탐색
    for i in range(idx+1, n):
         if not visited[i]:
            visited[i] = 1
            back(cnt+1, i)
            visited[i] = 0

n = int(input())
s = [list(map(int, input().split())) for _ in range(n)]
ans = 10**9

visited = [0] * n
back(0, 0)
print(ans)