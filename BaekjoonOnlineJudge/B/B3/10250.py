T = int(input())
for tc in range(1, T+1):
    H, W, N = map(int, input().split())
    num = N//H + 1
    floor = N % H
    if N % H == 0:
        num = N // H
        floor = H
    print(f'{floor*100+num}')