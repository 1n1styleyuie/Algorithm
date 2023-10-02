T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    wi = list(map(int, input().split()))
    ti = list(map(int, input().split()))
    wi.sort(reverse=True)
    ti.sort(reverse=True)
    cnt = 0
    while wi and ti:
        if ti[0] >= wi[0]:
            cnt += wi[0]
            wi.pop(0)
            ti.pop(0)
        else:
            wi.pop(0)
    print(f'#{tc} {cnt}')