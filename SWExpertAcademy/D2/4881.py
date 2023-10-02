# 시작점, 종료점, 더해질 변수의 초기값
def col_minimum(i, N, sum_min):
    global min_num # 전역변수 설정
    if sum_min > min_num: # 만약 더한값이 가장 작은값보다 크면 함수 종료
        return

    if i == N: # 종료점에 도달하였을 때
        if min_num > sum_min: # 가장 작은값보다 더한값이 크다면
            min_num = sum_min # 바꿔주고 함수 종료
        return
    else: # 그 외 경우 재귀호출
        for j in range(i, N): # 자신부터 오른쪽 끝까지
            A[i], A[j] = A[j], A[i] # 서로 자리를 바꿔주고
            col_minimum(i+1, N, sum_min+arr[i][A[i]]) # 재귀 호출
            A[i], A[j] = A[j], A[i] # 다시 원래의 자리로


T = int(input())
for tc in range(1, T+1):
    N = int(input()) # 배열의 길이
    arr = [list(map(int, input().split())) for _ in range(N)] # 배열 input
    min_num = 1e9 # 가장 큰 값을 넣어 작은 값을 받을 수 있도록 설정
    A = [i for i in range(N)] # 함수에서 자리바꿈을 하기위해 배열 생성
    col_minimum(0, N, 0) # 함수 호출(시작, 끝, 초기값)
    print(f'#{tc}', min_num) # 결과 출력