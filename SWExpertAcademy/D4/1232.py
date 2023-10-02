def calculate(node):
    if node:
        calculate(left[node])
        calculate(right[node])
        if tree[node] == '+':
            tree[node] = int(tree[left[node]]) + int(tree[right[node]])
        elif tree[node] == '-':
            tree[node] = int(tree[left[node]]) - int(tree[right[node]])
        elif tree[node] == '*':
            tree[node] = int(tree[left[node]]) * int(tree[right[node]])
        elif tree[node] == '/':
            tree[node] = int(tree[left[node]]) // int(tree[right[node]])


T = 10
for tc in range(1, T + 1):
    N = int(input())
    tree = [0] * (N + 1)
    left = [0] * (N + 1)
    right = [0] * (N + 1)

    for _ in range(N):
        arr = input().split()
        tree[int(arr[0])] = arr[1]

        if len(arr) == 4:
            left[int(arr[0])] = int(arr[2])
            right[int(arr[0])] = int(arr[3])

    calculate(1)

    print(f'#{tc} {tree[1]}')