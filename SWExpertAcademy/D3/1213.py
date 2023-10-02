for tc in range(1, 11):
    test_case = input()
    p = input()
    t = input()

    M = len(p)
    N = len(t)

    def BruteForce(p, t):
        i = 0
        j = 0
        cnt = 0

        while j < M and i < N:
            if t[i] != p[j]:
                i = i - j
                j = -1
            i = i + 1
            j = j + 1
            if j == M:
                cnt += 1
                j = 0
        return cnt

    result = BruteForce(p, t)
    print(f'#{test_case} {result}')