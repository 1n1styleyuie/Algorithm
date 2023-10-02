def dfs(S, G, V, adj_m):
    stack = [] # stack 생성
    visited = [0] * (V+1) # 방문하면 1로 변경
    stack.append(S) # 시작지점 stack에 추가
    while stack:
        n = stack.pop() # stack에서 pop하여 비교할 대상 설정
        if visited[n] == 0: # 만약 방문한 곳이 아니라면
            visited[n] = 1 # 방문한것으로 바꿔줌
            for w in range(1, V+1): # 모든 정점에 대해서
                if adj_m[n][w] == 1: # n과 w가 연결되어있고
                    if visited[w] == 0: # w를 방문한 적이 없으면
                        if w == G: # 찾아갈 지점이 w와 같다면
                            return 1 # 1 값을 반환
                        stack.append(w) # stack에 추가
    return 0 # 못찾고 끝나게 되면 0을 반환

T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    adj_m = [[0]*(V+1) for _ in range(V+1)]
    for _ in range(E):
        a1, a2 = map(int, input().split())
        adj_m[a1][a2] = 1
    S, G = map(int, input().split())
    res = dfs(S, G, V, adj_m)
    print(f'#{tc} {res}')