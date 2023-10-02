import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N, Q = map(int, input().split())
    box_list = [0 for _ in range(N)] # 리스트에 0을 저장

    for i in range(1, Q+1): # Q개의 작업만큼 수행
        L, R = map(int, input().split())
        for j in range(L-1, R): # 좌우 값만큼 값을 대입
            box_list[j] = i

    print(f'#{tc}', *box_list)