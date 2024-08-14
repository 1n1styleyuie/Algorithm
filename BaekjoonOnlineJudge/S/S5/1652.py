import sys
input = sys.stdin.readline

n = int(input())
arr = [list(input()) for _ in range(n)]
row_cnt = 0
col_cnt = 0


for i in range(n):
    cnt = 0
    for j in range(n):
        # 누울수 있는 자리일 경우 cnt + 1
        if arr[i][j] == '.':
            cnt += 1
            # 누울수 있는 자리인데 끝자리일 경우
            # cnt가 2 이상일 경우 누울수 있는 공간수에 +1하고 cnt 초기화
            if j == n-1:
                if cnt >= 2:
                    row_cnt += 1
                    cnt = 0
                else:
                    cnt = 0
        # 누울 수 없는 자리일 때 cnt가 2 이상일 경우
        # 누울 수 있는 공간 수에 +1 하고 cnt 초기화
        elif arr[i][j] == 'X':
            if cnt >= 2:
                row_cnt += 1
            cnt = 0


for j in range(n):
    cnt = 0
    for i in range(n):
        if arr[i][j] == '.':
            cnt += 1
            if i == n-1:
                if cnt >= 2:
                    col_cnt += 1
                    cnt = 0
                else:
                    cnt = 0
        elif arr[i][j] == 'X':
            if cnt >= 2:
                col_cnt += 1
            cnt = 0


print(row_cnt, col_cnt)