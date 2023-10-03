import sys
input = sys.stdin.readline

arr = [list(input().strip()) for _ in range(5)]
stack = []
for j in range(15):
    for i in range(5):
        try:
            stack.append(arr[i][j])
        except:
            continue
print(''.join(stack))