import sys
sys.stdin = open("input.txt", "r")
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    max_v = -1e9 # 최고값을 찾기 위해 임의의 가장 작은값으로 설정
    for i in range(N): # N * N 행렬
        for j in range(N):
            s = arr[i][j] # 이중 for문을 통해 리스트 중 하나의 값을 s로 설정
            count = 0 # 파리를 몇마리나 잡았는지를 확인하기 위해 변수 생성
            for k in range(0, M): # 파리채의 크기가 M * M
                for h in range(0, M):
                    ni, nj = i + k, j + h
                    # k와 h의 범위가 0부터 M-1까지 바꿔가며 배열 내 값을 탐색
                    if 0 <= ni < N and 0 <= nj < N: # 배열을 벗어나지 않으면
                        count += arr[ni][nj] # 잡은 파리수를 count에 저장
            if max_v < count: # max_v의 값이 count보다 작을 경우
                max_v = count # count의 값을 max_v에 저장
    print(f'#{tc} {max_v}')
