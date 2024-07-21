#15663

n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
res = []
visited = [0] * n

def dfs():
    idx = 0
    if len(res) == m:
        print(*res)
        return
    
    for i in range(n):
        if idx != arr[i] and not visited[i]:
            res.append(arr[i])
            visited[i] = 1
            idx = arr[i]
            dfs()
            res.pop()
            visited[i] = 0

dfs()
