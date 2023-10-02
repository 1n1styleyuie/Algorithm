import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    cnt = 0
    for y in range(N+1): # 원의 반지름 크기만큼 반복
        x = int((N ** 2 - y ** 2) ** 0.5) # 주어진 식으로 계산
        cnt += x # 카운트

    result = cnt * 4 + 1 # 원점을 포함하여 4분면을 모두 곱하여 값을 출력
    print(f'#{tc} {result}')
