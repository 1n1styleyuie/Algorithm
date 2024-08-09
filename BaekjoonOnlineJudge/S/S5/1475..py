# 1475 s5

n = int(input())
arr = [0] * 10
for i in str(n):
    if i == '9' or i == '6':
        # 9와 6의 수가 같을 댄 6에 +1, 다를때 9에 +1
        if arr[6] == arr[9]:
            arr[6] += 1
        else:
            arr[9] += 1
    else:
        arr[int(i)] += 1

print(max(arr))