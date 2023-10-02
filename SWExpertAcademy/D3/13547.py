#import sys
#sys.stdin = open("sample_input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    text = input()
    # print(str)

    cnt = 0
    for c in text:
        if c== 'x':
            cnt = cnt + 1

    if cnt >= 8:
        ret = "NO"
    else:
        ret = "YES"
    print("#"+str(test_case)+" "+ret)

    # ///////////////////////////////////////////////////////////////////////////////////
