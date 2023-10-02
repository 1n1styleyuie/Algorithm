T = int(input())
for tc in range(1, T+1):
    N = int(input())
    count = 0
    lst = [[0] * 10 for _ in range(10)]
    for i in range(N):
        r1, c1, r2, c2, color = map(int, input().split())
        for i in range(r1, r2+1):
            for j in range(c1, c2+1):
                if color == 1:
                    lst[i][j] += 1
                elif color == 2:
                    lst[i][j] += 2


    for i in range(10):
        for j in range(10):
            if lst[i][j] == 3:
                count += 1


    print(f'#{tc} {count}')