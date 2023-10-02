N = int(input())
for _ in range(N):
    arr = list(input())
    cnt = 1
    res = 0
    for i in range(len(arr)):
        if arr[i] == 'O':
            res += cnt
            cnt += 1
        else:
            cnt = 1
    print(res)