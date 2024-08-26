# 13023 g5

import sys
input = sys.stdin.readline

def dfs(i, cnt):
    global ans
    '''
    A, B, C, D, E
    한 친구에서 시작해서 4명의 친구를 중복없이 이어질 수 있게 하는 문제이다.
    예제 입력 2에서 0 - 1 - 2 - 3 - 0이고 1 - 4이다. 
    해당 예제에서 4에서 출발할 경우 4 - 1 - 2 - 3 - 0 으로 중복 없이 5명이 연결될 수 있다.
    따라서 연결할 수 있는 경우 방문체크를 하고 카운트를 하여 카운트가 4를 넘을 경우 ans를 True로 리턴하면 된다.
    '''
    if cnt >= 4:
        ans = True
        return
    for a in adj_l[i]:
        if not visited[a]:
            visited[a] = 1
            dfs(a, cnt+1)
            visited[a] = 0
    return



n, m = map(int, input().split())
adj_l = [[] for _ in range(n)]
visited = [0] * n
ans = False

# 인접리스트 생성
for _ in range(m):
    a, b = map(int, input().split())
    adj_l[a].append(b)
    adj_l[b].append(a)

for i in range(n):
    # 방문하지 않은 곳 탐색하여
    if not visited[i]:
        # 방문체크 후 dfs 호출
        visited[i] = 1
        dfs(i, 0)
        # 함수 호출이 끝난 후 0으로 바꿔줌
        visited[i] = 0
        # 만약 결과값이 True가 나왔다면 반복문 중단
        if ans:
            break

if ans:
    print(1)
else:
    print(0)