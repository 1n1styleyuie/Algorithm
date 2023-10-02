T = int(input())

for test_case in range(1, T+1):
    K, N, M = map(int, input().split())
    station = list(map(int, input().split()))
    count = 0

    state = 0

    while True:
        if state + K >= N:
            break

        found_station = False

        for j in range(state + K, state, -1):

            if j in station:
                count += 1
                state = j
                found_station = True
                break
        if found_station == False:
            count = 0
            break
    print(f'#{test_case} {count}')