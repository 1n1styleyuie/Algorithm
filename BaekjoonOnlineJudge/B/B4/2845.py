l, p = map(int, input().split())
arr = list(map(int, input().split()))
res = []
num = l*p
for i in range(5):
    res.append(arr[i]-num)

print(*res)