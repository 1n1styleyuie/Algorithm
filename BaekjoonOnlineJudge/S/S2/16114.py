# 16114 s2
import sys
input = sys.stdin.readline

x, n = map(int, input().split())

# n이 0일때 x가 양수이면 INFINTE를 출력한다.
# 그 외의 경우 에러가 아닌 카운트가 0인 상태로 종료가 된다.
if n == 0:
    if x > 0:
        print('INFINITE')
    else:
        print('0')
# n이 1일때 x가 음수이면 INFINTE를 출력한다.
# 그 외의 경우 에러가 아닌 카운트가 0인 상태로 종료가 된다.
elif n == 1:
    if x < 0:
        print('INFINITE')
    else:
        print('0')
else:
    # n이 2이상이면서 홀수일 경우는 부정 연산자가 적용된 것으로 에러를 출력
    if n % 2 == 1:
        print('ERROR')
    # n이 2이상이면서 짝수일 경우 카운트하여 출력
    else:
        cnt = 0
        divide = n // 2
        x -= divide
        while 0 < x:
            x -= divide
            cnt += 1
        print(cnt)