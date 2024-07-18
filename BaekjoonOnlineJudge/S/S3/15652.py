# 15652

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
res = []

def dfs(start):
    if len(res) == M:
        print(*res)
        return

    for i in range(start, N+1):

        res.append(i)
        dfs(i)
        res.pop()

dfs(1)