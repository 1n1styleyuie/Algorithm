for test_case in range(1, 11):
    # ///////////////////////////////////////////////////////////////////////////////////
    N = int(input())
    arr = list(map(int, input().split()))
    left_side = 0
    right_side = 0
    high_state = 0
    count = 0
    for i in range(2, N-2):
        if arr[i-1] < arr[i-2]:
            left_side = arr[i-2]
        else:
            left_side = arr[i-1]
        if arr[i+1] < arr[i+2]:
            right_side = arr[i+2]
        else:
            right_side = arr[i+1]

        if arr[i] > left_side and arr[i] > right_side:
            if left_side > right_side:
                high_state = left_side
            else:
                high_state = right_side

            count += (arr[i] - high_state)

    print(f'#{test_case} {count}')

    # ///////////////////////////////////////////////////////////////////////////////////