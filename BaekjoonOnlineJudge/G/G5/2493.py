# 2493 g5
import sys
input = sys.stdin.readline


n = int(input())
arr = list(map(int, input().split()))
res = [0] * n

stack = []

'''
앞에서 부터 탐색을 하면서 stack에 저장한다.

stack에 하나이상 존재할 경우 
현재 위치에 있는 탑의 높이하고 비교하였을 때 stack에 마지막에 저장한 탑의 높이가 클 경우
현재 위치의 탑은 가장 먼저 만나는 탑이 stack에 마지막에 저장된 탑이 된다. 
따라서 stack의 마지막 저장된 탑의 인덱스를 res에 저장한다.

만약 현 위치 탑의 높이가 클 경우에는 stack을 pop하여 stack에 있는 탑을 탐색하여 확인한다.
초기값을 0으로 설정했기 때문에 현 위치 탑보다 큰 값이 없어도 0으로 표기하면 된다.

'''

for i in range(n):
    while stack:
        if stack[-1][1] > arr[i]:
            res[i] = stack[-1][0] + 1
            break
        else:
            stack.pop()
    stack.append((i, arr[i]))

print(*res)