import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(str, input().split())) for _ in range(N)]
    num_list = [[''] * N for _ in range(N)] # 문자열인 빈 리스트를 생성

    # 90도 회전
    for j in range(N):
        for i in range(N):
            num_list[j][0] += arr[N-1-i][j] # 문자열 더하기

    # 180도 회전
    for i in range(N):
        for j in range(N):
            num_list[i][1] += arr[N-1-i][N-1-j] # 문자열 더하기

    # 270도 회전
    for j in range(N):
        for i in range(N):
            num_list[j][2] += arr[i][N-1-j] # 문자열 더하기

    print(f'#{tc}')
    for i in range(N):
        print(*num_list[i]) # 언패킹으로 출력