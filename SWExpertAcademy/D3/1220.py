T = 10
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    cnt = 0
    for i in range(N):
        for j in range(N):
            # 극성이 있는곳을 찾으면 그곳부터 다시 탐색
            if arr[i][j] == 1:
                for k in range(i+1, N):
                    # 같은 극성이 두개이더라도 다른 극성과 만났을때 카운트는 하나만 증가한다.
                    # 따라서 카운트하지않고 k에 대한 반복문을 멈춘다.
                    if arr[k][j] == 1:
                        break
                    # 서로 다른 극성끼리 만났기 때문에 카운트하고 반복문을 멈춘다.
                    elif arr[k][j] == 2:
                        cnt += 1
                        break

    print(f'#{tc} {cnt}')