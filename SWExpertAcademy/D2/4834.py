T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    N = int(input())
    num1 = int(input())
    c = [0] * 12

    for i in range(N):
        c[num1 % 10] += 1  # 주어진 자릿수를 카운트에 저장
        num1 //= 10  # 10으로 나누어 다음 자릿수로 반환

    max_count = 0
    max_idx = 0
    for i in range(len(c)):
        if max_count <= c[i]:
            max_count = c[i]
            max_idx = i


    print(f'#{test_case} {max_idx} {max_count}')
    # ///////////////////////////////////////////////////////////////////////////////////