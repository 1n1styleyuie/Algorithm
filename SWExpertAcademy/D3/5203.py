def f():
    for i in range(10):
        if p1[i] >= 3:
            return 1
        if p1[i] and p1[i+1] and p1[i+2]:
            return 1
        if p2[i] >= 3:
            return 2
        if p2[i] and p2[i+1] and p2[i+2]:
            return 2


T = int(input())
for tc in range(1, T+1):
    arr = list(map(int, input().split()))
    p1 = [0]*12
    p2 = [0]*12
    res = 0
    for i in range(6):
        p1[arr[i*2]] += 1
        if f():
            res = f()
            break
        p2[arr[i*2+1]] += 1
        if f():
            res = f()
            break

    print(f'#{tc} {res}')