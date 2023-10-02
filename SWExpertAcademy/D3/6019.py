import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    D, A, B, F = map(int, input().split())
    kill_time = D / (A + B) # 파리가 죽는 시간
    result = F * kill_time # 죽는 시간동안 간 거리
    print(f'#{tc} {result}')