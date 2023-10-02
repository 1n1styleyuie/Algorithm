#import sys
#sys.stdin = open("sample_input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    lst = list(input())
    maxv = minv = int(''.join(lst))
    for i in range(len(lst) - 1):
        for j in range(i + 1, len(lst)):
            lst[i], lst[j] = lst[j], lst[i]
            if maxv < int("".join(lst)):
                maxv = int("".join(lst))
            if lst[0] != '0' and minv > int("".join(lst)):
                minv = int("".join(lst))
            lst[i], lst[j] = lst[j], lst[i]
    print(f"#{test_case} {minv} {maxv}")
    # ///////////////////////////////////////////////////////////////////////////////////