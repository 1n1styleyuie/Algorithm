N = int(input())
arr = input()
lr, sk = 0, 0
cnt = 0
for i in arr:
    if i == 'L':
        lr += 1
    elif i == 'R':
        if lr > 0:
            cnt += 1
            lr -= 1
        else:
            break
    elif i == 'S':
        sk += 1
    elif i == 'K':
        if sk > 0:
            cnt += 1
            sk -= 1
        else:
            break
    else:
        cnt += 1
print(cnt)
