# 2630 s2
import sys
input = sys.stdin.readline

# r = 행, c = 열, n = 길이
def f(r, c, n):
    global white, blue
    color = arr[r][c]
    # n 길이만큼 탐색을 했을 때 다른색이 있을 경우
    # 해당 사분면으로 재귀를 통해 다시 탐색 후 return
    for i in range(r, r + n):
        for j in range(c, c + n):
            if color != arr[i][j]:
                # 2사분면
                f(r, c, n // 2)
                # 1사분면
                f(r, c + n // 2, n // 2)
                # 3사분면
                f(r + n // 2, c, n // 2)
                # 4사분면
                f(r + n // 2, c + n // 2, n // 2)
                return
    # n 길이 만큼 탐색을 했을 때 다른색이 없을 경우
    # 해당 색의 카운트를 +1 해준다.
    if color == 0:
        white += 1
    else:
        blue += 1
    return


n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
blue = 0
white = 0

f(0, 0, n)

print(white)
print(blue)