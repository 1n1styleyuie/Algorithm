N, M = map(int, input().split())
num = N*M
for i in range(1, num+1):
    if i % M == 0:
        print(i, end='\n')
    else:
        print(i, end=' ')