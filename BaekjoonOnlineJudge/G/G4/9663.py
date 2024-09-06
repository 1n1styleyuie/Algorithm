# 9663 g4
import sys
input = sys.stdin.readline

def check(r):
    for i in range(r):
        # 같은 열에 있거나 대각선에 있는 경우 True반환
        if arr[r] == arr[i] or abs(arr[r] - arr[i]) == abs(r - i):
            return True
    return False


def backtracking(r):
    # r은 행을 의미
    global cnt
    if r == n:
        cnt += 1
        return
    for c in range(n):
        arr[r] = c
        if not check(r):
            backtracking(r+1)



n = int(input())
cnt = 0
arr = [0] * n
backtracking(0)
print(cnt)