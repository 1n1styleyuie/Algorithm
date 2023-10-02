import sys
sys.stdin = open('input.txt')

# T = int(input())
# for tc in range(1, T+1):
#     sudoku = [list(map(int, input().split())) for _ in range(10)]
#     #행 순회
#     for i in range(10):
#         col = []
#         for j in range(10):
#             col.append(sudoku[i][j])
#         for k in range(1, 10):
#             if k not in col:
#                 print(f'#{tc} 0')
#
#     for j in range(10):
#         row = []
#         for i in range(10):
#             row.append(sudoku[i][j])
#         for k in range(1, 10):
#             if k not in row:
#                 print(f'#{tc} 0')
#
#     for h in range(0, 10, 3):
#         box = []
#         for i in range(3):
#             for j in range(3):
#                 box.append(sudoku[i+h][j+h])
#         for k in range(1, 10):
#             if k not in row:
#                 print(f'#{tc} 0')
#
#     print(f'#{tc} 1')
# #
# def sudoku(arr):
#     for i in range(9):
#         cnt = [0] * 10
#         for j in range(9):
#             cnt[arr[i][j]] += 1
#         for k in range(1, 10):
#             if cnt[k] == 0:
#                 return 0

#
#
# T = int(input())
# for tc in range(1, T+1):
#     arr = [list(map(int, input().split())) for _ in range(9)]
#     ans = sudoku(arr) # 스도쿠가 완성되면 1, 아니면 0
#     print(f'#{tc} {ans}')
#
T = int(input())
for tc in range(1, T + 1):
    arr = [list(map(int, input().split())) for _ in range(9)]

    ans = 1
    flg = True  # 스도쿠가 아닐 경우 반복문을 종료하기 위해 flag 생성

    for row in arr:  # 가로 탐색
        for i in range(9):
            for j in range(i + 1, 9):
                if row[i] == row[j]:
                    ans = 0
                    flg = False
                    break
            if not flg:
                break

        if not flg:
            break

    if flg:
        for j in range(9):  # 세로 탐색
            for i in range(9):
                for k in range(i + 1, 9 - i):
                    if arr[i][j] == arr[i + k][j]:
                        ans = 0
                        flg = False
                        break
                if not flg:
                    break
            if not flg:
                break

    if flg:
        cor = [0, 3, 6]  # 정사각형 왼쪽 위 인덱스 설정
        for i in cor:  # 정사각형 탐색
            for j in cor:
                lst = []
                for k in range(3):
                    lst.append(arr[i + k][j + k])

                if len(lst) != len(set(lst)):
                    ans = 0
                    flg = False
                    break


    print(f'#{tc}', ans)