import sys
sys.stdin = open('input.txt')


def length(n):
    cnt = 0
    for _ in n:
        cnt += 1
    return cnt


T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    max_cnt = 0

    # 행 순회
    for i in range(N):
        stack1 = []
        for j in range(M):
            # 배열에 있는 값이 1이라면 스택에 추가
            if arr[i][j] == 1:
                stack1.append(arr[i][j])
                # 만약 스택의 길이가 max_cnt보다 클 경우 값을 바꿔줌
                if max_cnt < length(stack1):
                    max_cnt = length(stack1)
            # 0일 경우 스택을 초기화
            else:
                stack1.clear()

    # 열 순회
    for j in range(M):
        stack2 = []
        for i in range(N):
            # 배열에 있는 값이 1이라면 스택에 추가
            if arr[i][j] == 1:
                stack2.append(arr[i][j])
                # 만약 스택의 길이가 max_cnt보다 클 경우 값을 바꿔줌
                if max_cnt < length(stack2):
                    max_cnt = length(stack2)
            # 0일 경우 스택을 초기화
            else:
                stack2.clear()

    print(f'#{tc} {max_cnt}')