import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    count_a = 0
    count_b = 0
    count_c = 0
    count_d = 0
    count_e = 0

    while N > 1: # N이 1보다 클때 반복
        if N % 2 == 0: # 2로 나눌수 있는 횟수를 카운트
            N //= 2
            count_a += 1
        elif N % 3 == 0: # 3로 나눌수 있는 횟수를 카운트
            N //= 3
            count_b += 1
        elif N % 5 == 0: # 5로 나눌수 있는 횟수를 카운트
            N //= 5
            count_c += 1
        elif N % 7 == 0: # 7로 나눌수 있는 횟수를 카운트
            N //= 7
            count_d += 1
        elif N % 11 == 0: # 11로 나눌수 있는 횟수를 카운트
            N //= 11
            count_e += 1
    # 각각 카운트 한 값을 출력
    print(f'#{tc} {count_a} {count_b} {count_c} {count_d} {count_e}')