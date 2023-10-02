import sys
sys.stdin = open('input.txt')

for tc in range(1, 11):
    test_case = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]

    row = arr[99].index(2) # 마지막 행에서 값이 2인 인덱스를 찾아 저장
    col = 99 # 아래에서 부터 올라가기 위해 행을 99로 설정

    while col:
        if row != 99 and arr[col][row+1]: # 99를 벗어나지 않는 범위 내에서
            arr[col][row] = 0 # 지금 있는 곳을 0으로 만들어 다시 돌아오지 않도록 함
            row += 1 # 위치를 이동
        elif row != 0 and arr[col][row-1]: # 0을 벗어나지 않는 범위 내에서
            arr[col][row] = 0 # 지금 있는 곳을 0으로 만들어 다시 돌아오지 않도록 함
            row -= 1 # 위치를 이동
        else: # 좌우에 1이 없는 경우
            col -= 1 # 행을 이동

    print(f'#{test_case}', row)
