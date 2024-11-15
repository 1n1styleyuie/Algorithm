# 1347 s2
import sys
input = sys.stdin.readline

n = int(input())
ss = input().rstrip()


dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

x, y = 0, 0

direction = 0

tmp = []
tmp.append([x, y])

for s in ss:
    if s == 'F':
        x += dx[direction % 4]
        y += dy[direction % 4]
        tmp.append([x, y])
    elif s == 'R':
        direction += 1
    else:
        direction += 3

x_idx = []
y_idx = []
for t in tmp:
    x_idx.append(t[0])
    y_idx.append(t[1])

x_length = len(set(x_idx))
y_length = len(set(y_idx))

if min(x_idx) < 0:
    x_c = abs(min(x_idx))
else:
    x_c = 0

if min(y_idx) < 0:
    y_c = abs(min(y_idx))
else:
    y_c = 0

maze = [[0] * y_length for _ in range(x_length)]

for t in tmp:
    maze[t[0]+x_c][t[1]+y_c] = '.'

for i in range(x_length):
    if i != 0:
        print()
    for j in range(y_length):
        if maze[i][j] == 0:
            print('#', end='')
        else:
            print(maze[i][j], end='')