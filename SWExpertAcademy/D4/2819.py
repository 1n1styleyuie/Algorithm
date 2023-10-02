dy = [0, 0, 1, -1]
dx = [1, -1, 0, 0]
def dfs(y, x,  number):
    if len(number) == 7:
        # 추가적인 작업
        result.add(number)
        return

    for k in range(4):
        ny = y + dy[k]
        nx = x + dx[k]

        # 갈 수 없는 위치이면 continue
        if ny < 0 or ny >= 4:
            continue

        if nx < 0 or nx >= 4:
            continue

        # 갈 수 있다면, 다음 위치로 이동
        dfs(ny, nx, number+maps[ny][nx])



T = int(input())
for tc in range(1, T+1):
    # 서로 다른 수를 합친다 => 문자열이 더 좋다.
    maps = [input().split() for _ in range(4)]

    # 7자리 수를 중복 제거하여 저장
    result = set()

    # 시작지점 == 모두 보아야 한다.
    for i in range(4):
        for j in range(4):
            dfs(i, j, maps[i][j])

    print(f'#{tc} {len(result)}')