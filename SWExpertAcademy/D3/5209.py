def f(i, N, total):
    global minimum_price
    # 이미 계산한 값이 가장 작은 값보다 크다면
    if total > minimum_price:
        return
    # 모두 탐색을 했을 때
    if i == N:
        if total < minimum_price:
            minimum_price = total
        return
    # 다음 탐색을 위해
    for j in range(N):
        # 방문하지 않는 곳을 찾아서
        if not visited[j]:
            # 방문을 하고
            visited[j] = 1
            # 재귀호출
            f(i+1, N, total+arr[i][j])
            # 백트래킹
            visited[j] = 0


T = int(input())
for tc in range(1, T+1):
    # N : 제품수, arr : 제품당 공장별 생산비용, visited : 방문목록
    # minimum_price : 가장 작은 값을 담기 위한 변수
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [0] * N
    minimum_price = 1e9
    f(0, N, 0)
    print(f'#{tc} {minimum_price}')