def BruteForce(p, t):
    i = 0
    j = 0
    cnt = 0
    M = len_count(p)
    N = len_count(t)

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


def len_count(s):
    len_cnt = 0
    for _ in s:
        len_cnt += 1
    return len_cnt


T = int(input())
for tc in range(1, T+1):
    word = input()
    sentence = input()
    max_cnt = -1e9
    len_word = len_count(word)
    for i in range(len_word):
        result = BruteForce(word[i], sentence)
        if max_cnt < result:
            max_cnt = result
    print(f'#{tc} {max_cnt}')