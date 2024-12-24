# 1817 s5
import sys
input = sys.stdin.readline


n, m = map(int, input().split())
cnt = 0
if n == 0:
    print(0)
else:
    # 차례대로 넣기때문에 정렬하지 않고 그냥 넣는다
    # 박스의 무게가 넘치는 경우 다음박스에 담는다.
    arr = list(map(int, input().split()))
    w = 0
    for a in arr:
        if w + a <= m:
            w += a
        else:
            w = a
            cnt += 1
    cnt += 1
    print(cnt)