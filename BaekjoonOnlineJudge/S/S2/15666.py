#15666

n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
res = []

def dfs(start):
    if len(res) == m:
        print(*res)
        return
    # 중복조합을 피하기 위해 temp변수 생성
    temp = 0
    for i in range(start, n):
        if temp != arr[i]:
            res.append(arr[i])
            temp = arr[i]
            dfs(i)
            res.pop()

dfs(0)
