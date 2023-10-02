# 17219
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
domain_dict = {}
for _ in range(N):
    a, b = input().split()
    domain_dict[a] = b

for _ in range(M):
    domain_find = input().strip()
    print(domain_dict[domain_find])
