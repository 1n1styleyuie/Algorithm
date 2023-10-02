import sys
input = sys.stdin.readline


N, K = map(int, input().split())
arr = [i for i in range(1, N+1)]
q = []
while arr:
    for i in range(K-1):
        arr.append(arr.pop(0))
    q.append(arr.pop(0))

print('<', end='')
for i in range(N-1):
    print(q[i], end=', ')
print(q[-1], end='')
print('>')