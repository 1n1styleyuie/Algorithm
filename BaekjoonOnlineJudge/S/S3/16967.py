# 16967 s3
import sys
input = sys.stdin.readline

h, w, x, y = map(int, input().split())
b = [list(map(int, input().split())) for _ in range(h+x)]

a = [[0] * w for _ in range(h)]

# 원래 배열은 h x w 크기이기 때문에 b에 저장되어 있는 원래 배열 크기만큼만 a에 저장한다.
for i in range(h):
    for j in range(w):
        a[i][j] = b[i][j]

# 겹치는 부분은 x에서 h만큼, y에서 w만큼 겹쳐져 있는 것이다.
# b로 배열을 만들때 b[i][j] = a[i][j] + a[i-x][j-y] 였기 떄문에
# a[i][j] = b[i][j] - a[i-x][j-y]로 다시 구할 수 있다.
for i in range(x, h):
    for j in range(y, w):
        a[i][j] = b[i][j] - a[i-x][j-y]

for i in range(len(a)):
    print(*a[i])