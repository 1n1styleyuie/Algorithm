# 2477 s2
import sys
input = sys.stdin.readline


x = []
y = []
s = []
k = int(input())
for _ in range(6):
    a, b = map(int, input().split())
    s.append((a, b))
    if a == 3 or a == 4:
        x.append(b)
    if a == 1 or a == 2:
        y.append(b)


minus = []
'''
방향이 같은 방향을 가리킬 경우 중간에 끼어있는 한 변은 안쪽으로 들어간 변이 된다.
따라서 중간에 있는 변의 길이를 저장하게 되면 가로와 세로 하나씩 저장이 된다.
전체 크기에서 빼면 구하고자 하는 넓이가 나오게 된다.

7
4 50
2 160
3 30
1 60
3 20
1 100

다음과 같이 주어지게 되면 3 1 3인 경우 한번 건너 뛰고 같은 방향이기 때문에 중간에 낀 1 60이 작은 사각형의 가로가 된다.
따라서 1 3 1에서도 한번 건너 뛰고 같은 방향이기 때문에 3 20이 작은 사각형의 세로가 된다.
'''
for i in range(6):
    if s[i][0] == s[(i+2)%6][0]:
        minus.append(s[(i+1)%6][1])


print(((max(x) * max(y)) - (minus[0] * minus[1])) * k)