S = input()
arr = [-1] * 26
for i in range(len(S)):
    num = ord(S[i]) - 97
    if arr[num] == -1:
        arr[num] = i
    else:
        continue
print(*arr)