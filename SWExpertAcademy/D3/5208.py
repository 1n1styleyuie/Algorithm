def f(now, finish, battery, change):
    global res
    # 이미 값이 크다면
    if change > res:
        return
    # 도착지를 왔거나 그 이상으로 갔다면
    if now >= finish:
        res = min(res, change)
        return
    # 배터리가 있는 경우
    if battery:
        f(now + 1, finish, battery - 1, change)
    # 배터리를 바꿔야 하는 경우
    f(now + 1, finish, N_battery[now] - 1, change + 1)


T = int(input())
for tc in range(1, T+1):
    N_list = list(map(int, input().split()))
    N = N_list[0]
    N_battery = N_list[1:]
    res = 1e9
    f(0, N-1, N_battery[0], 0)
    print(f'#{tc} {res}')