import sys
N, M = map(int, sys.stdin.readline().split())
n_list = set()
m_list = set()

for i in range(N):
    n_list.add(input())

for j in range(M):
    m_list.add(input())

result = sorted(list(n_list & m_list))
print(len(result))

for k in result:
    print(k)