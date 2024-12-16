# 1080 s1
import sys
input = sys.stdin.readline

'''
문제의 해결에 필요한 것은 3x3 행렬을 모두 뒤집는다는 것을 이해하면 된다.
a와 b에서 같은 위치에 있는 값이 다르다면 그 위치로부터 3x3 행렬을 만들어서 그 바꿔주면 된다.

3 4
0000
0010
0000
1001
1011
1001

입력1 예시처럼 나왔을 경우
(0, 0) 위치의 값이 0과 1로 다르기 떄문에 해당 위치부터 3x3행렬의 숫자를 바꿔주면 된다.
그렇게 할 경우 a 행렬은
1110
1101
1110
이 될 것이고 (0, 1) 위치의 값이 a와 b가 다르기 때문에 해당 위치부터 3x3 행렬 숫자를 바꾸면
1001
1010
1001
이 된다.
이럴 경우 a와 b의 배열이 같아졌기 때문에 2번 뒤집으면 b와 같아진다.

단 입력3번처럼
1 1
1
0
인 경우엔 -1이 맞지만
1 1
1
1
인 경우엔 0이기 때문에 예외처리를 해야 한다.
'''


def f(x, y):
    for i in range(x, x+3):
        for j in range(y, y+3):
            # 0이면 1로, 1이면 0으로 바꾸기
            if a[i][j] == '0':
                a[i][j] = '1'
            else:
                a[i][j] = '0'


n, m = map(int, input().split())
a = [list(input().rstrip()) for _ in range(n)]
b = [list(input().rstrip()) for _ in range(n)]

cnt = 0
if (n < 3 or m < 3) and a != b:
    cnt = -1
else:
    for r in range(n-2):
        for c in range(m-2):
            # 현 위치의 a와 b의 값이 동일하지 않을 경우에 바꾸기
            if a[r][c] != b[r][c]:
                f(r, c)
                cnt += 1


if a == b:
    print(cnt)
else:
    print(-1)