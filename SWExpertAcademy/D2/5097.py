T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    num_list = list(map(int, input().split()))
    for i in range(M):
        num_list.append(num_list.pop(0))
    print(f'#{tc} {num_list[0]}')