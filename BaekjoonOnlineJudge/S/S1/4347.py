# 4347 s1
import sys
input = sys.stdin.readline

def f(arr, x_count, o_count):
    if x_count != o_count and x_count != o_count + 1:
        return 'no'
    
    x_flg = check_win(arr, 'X')
    o_flg = check_win(arr, 'O')

    # X와 O 둘 다 승리한 경우, 유효하지 않음
    if x_flg and o_flg:
        return 'no'
    
    # X가 승리한 경우, X의 개수가 O보다 정확히 하나 많아야 함
    if x_flg and x_count != o_count + 1:
        return "no"
    
    # O가 승리한 경우, X와 O의 개수가 같아야 함
    if o_flg and x_count != o_count:
        return "no"
    
    return "yes"

def check_win(arr, player):
    # 행, 열, 대각선 체크
    # 그리드에 3x3으로 표시했을 때 한줄이 완성되는 위치의 인덱스를 저장
    # 해당 위치의 값들이 player와 모두 같을 경우 True 반환
    grid = [[0,1,2], [3,4,5], [6,7,8], [0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
    for i, j, k in grid:
        if arr[i] == arr[j] == arr[k] == player:
            return True
    return False

n = int(input())

for i in range(n):
    arr = []
    x_count = 0
    o_count = 0
    for _ in range(3):
        a, b, c = input().rstrip()
        # 카운트 세고 리스트에 저장
        # a, b, c를 리스트형태로 묶어서 저장하지 않은 이유는 3x3 그리드이기 때문에
        # 인덱스를 직접 입력해서 찾는것이 빠르다 생각하여 들어온 순서대로 저장
        if a == 'X':
            x_count += 1
        if b == 'X':
            x_count += 1
        if c == 'X':
            x_count += 1
        if a == 'O':
            o_count += 1
        if b == 'O':
            o_count += 1
        if c == 'O':
            o_count += 1
        arr.append(a)
        arr.append(b)
        arr.append(c)
    if i == n-1:
        pass
    else:
        input()
    print(f(arr, x_count, o_count))
