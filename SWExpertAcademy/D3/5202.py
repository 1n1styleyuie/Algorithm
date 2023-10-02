T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    # 끝난 시간순으로 정렬
    arr.sort(key=lambda x: x[1])
    # 정렬후 맨 앞에 있는 값을 먼저 시작했기 때문에 1 저장
    cnt = 1
    # 처음 위치
    j = 0

    # 반복을 통해 비교해서 카운트하고 끝나는 시간을 저장한다.
    for i in range(N):
        if arr[i][0] >= arr[j][1]:
            cnt += 1
            j = i

    print(f'#{tc} {cnt}')