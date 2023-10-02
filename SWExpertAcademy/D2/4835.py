T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    new_list = []
    for j in range(N-M+1):
        result = 0
        for k in range(j, j+M):
            result += arr[k]
        new_list.append(result)

    print('#{} {}'.format(test_case, max(new_list)-min(new_list)))