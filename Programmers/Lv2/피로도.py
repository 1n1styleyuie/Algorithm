answer = 0
def dfs(k, cnt, dungeons, visited):
    global answer
    # 최대로 많이 돌 수 있는 경우를 answer에 저장
    if cnt > answer:
        answer = cnt
    
    for i in range(len(dungeons)):
        if not visited[i] and k >= dungeons[i][0]:
            visited[i] = 1 # 방문
            dfs(k-dungeons[i][1], cnt + 1, dungeons, visited)
            visited[i] = 0 # 초기화


def solution(k, dungeons):
    global answer
    visited = [0] * len(dungeons)
    dfs(k, 0, dungeons, visited)   
    return answer

