# 16235 g3
'''
Python3으로 제출하게 되면 시간초과가 납니다.
Pypy3으로 제출하면 시간초과 없이 통과됩니다.
'''
import sys
input = sys.stdin.readline
from collections import deque


n, m, k = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(n)]
tree = [[[] for _ in range(n)] for _ in range(n)]
nutrient = [[5]*n for _ in range(n)]


for _ in range(m):
    x, y, z = map(int, input().split())
    tree[x-1][y-1].append(z)


for _ in range(k):
    for i in range(n):
        for j in range(n):
            '''
            봄에는 나무가 나이만큼 양분을 먹고 나이가 1 증가한다.
            이때 나이가 어린 나무부터 양분을 먹기 때문에 정렬하여 양분을 먹는다.
            
            나이가 어린 나무부터 양분을 줬기 때문에 양분보다 나이가 많았던 나무들은
            여름이 되어 전부 양분으로 변하게 된다.
            '''
            tree[i][j].sort()
            for k in range(len(tree[i][j])):
                if nutrient[i][j] >= tree[i][j][k]:
                    nutrient[i][j] -= tree[i][j][k]
                    tree[i][j][k] += 1
                else:
                    while k < len(tree[i][j]):
                        nutrient[i][j] += (tree[i][j].pop()//2)
                    break

    
    # 가을에는 나무가 번식하여 나무의 나이가 5의 배수일 경우 인접한 8칸에 나이가 1인 나무가 생긴다.
    delta = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]
    for i in range(n):
        for j in range(n):
            for k in range(len(tree[i][j])):
                if tree[i][j][k] % 5 == 0:
                    for di, dj in delta:
                        ni, nj = i+di, j+dj
                        if 0<=ni<n and 0<=nj<n:
                            tree[ni][nj].append(1)                

    # 겨울에 양분을 추가하는 과정이다.         
    for i in range(n):
        for j in range(n):
            nutrient[i][j] += A[i][j]   
            

ans = 0
for i in range(n):
    for j in range(n):
        ans += len(tree[i][j])


print(ans)


