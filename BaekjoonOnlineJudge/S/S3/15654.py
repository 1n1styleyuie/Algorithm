# 15654
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
lst = list(map(int, input().split()))
lst.sort()
res = []

def dfs(start):
    if len(res) == M:
        print(*res)
        return
    
    for i in lst:
        if i not in res:
            res.append(i)
            dfs(i+1)
            res.pop()
    
dfs(lst[0])