# 15650

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
res = []

def dfs(start):
    if len(res) == M:
        print(*res)
        return

    for i in range(start, N+1):
        if i not in res:
            res.append(i)
            dfs(i+1)
            res.pop()

dfs(1)