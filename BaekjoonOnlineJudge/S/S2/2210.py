# 2210 s2
import sys
input = sys.stdin.readline

delta = [[0, 1], [0, -1], [1, 0], [-1, 0]]

'''
이 문제에서 범위가 5x5로 크지 않기 때문에 리스트에 넣고 in 연산자를 써도 된다.
그리고 갔던 곳을 다시 가서 숫자를 만들 수 있기 떄문에 방문체크를 하지 않고 탐색을 한다.
'''


def dfs(i, j, number):
    if len(number) == 6:
        if number not in ans:
            ans.append(number)
        return

    
    for di, dj in delta:
        ni, nj = i+di, j+dj
        if 0 <= ni < 5 and 0 <= nj < 5:
            dfs(ni, nj, number + arr[ni][nj])



arr = [list(map(str, input().split())) for _ in range(5)]

ans = []

for i in range(5):
    for j in range(5):
        dfs(i, j, arr[i][j])

print(len(ans))