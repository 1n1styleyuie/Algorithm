# 2580 g4
import sys
input = sys.stdin.readline


def row(n, x):
    for j in range(9):
        if arr[x][j] == n:
            return False
    return True


def col(n, y):
    for i in range(9):
        if arr[i][y] == n:
            return False
    return True


def sqaure(n, x, y):
    x = x // 3 * 3
    y = y // 3 * 3
    for i in range(3):
        for j in range(3):
            if arr[i + x][j + y] == n:
                return False
    return True


def f(cnt):
    if cnt == len(lst):
        for a in range(9):
            print(*arr[a])
        exit()
    
    x = lst[cnt][0]
    y = lst[cnt][1]

    for n in range(1, 10):
        if row(n, x) and col(n, y) and sqaure(n, x, y):
            arr[x][y] = n
            f(cnt+1)
            arr[x][y] = 0


arr = [list(map(int, input().split())) for _ in range(9)]
lst = []
for i in range(9):
    for j in range(9):
        if arr[i][j] == 0:
            lst.append((i, j))

f(0)