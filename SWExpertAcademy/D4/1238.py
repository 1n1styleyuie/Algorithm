def bfs(start):
    q = []
    visited = [0] * 101
    q.append(start)
    visited[start] = 1
    # 최대 숫자와, 최대 깊이를 저장할 변수
    max_number = start
    max_depth = 1
    while q:
        now = q.pop(0)
        for to in graph[now]:
            if visited[to]:
                continue

            # 기존 방문보다 한번 더 갔다.
            visited[to] = visited[now] + 1
            # 한 단계 깊은 곳으로 가거나
            # 깊이는 같은데, 숫자가 더 크다면
            # max값을 초기화
            if max_depth < visited[to] or (max_depth == visited[to] and max_number < to):
                max_depth = visited[to]
                max_number = to
            q.append(to)
    return max_number


T = 10
for tc in range(1, T+1):
    n, start = map(int, input().split())
    tmp_list = list(map(int, input().split()))
    graph = [[] for _ in range(101)]
    for i in range(0, n, 2):
        f = tmp_list[i]
        t = tmp_list[i + 1]
        graph[f].append(t)

    res = bfs(start)
    print(f'#{tc} {res}')