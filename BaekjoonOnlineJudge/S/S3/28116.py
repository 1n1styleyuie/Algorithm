# 28116 s3
import sys
input = sys.stdin.readline


n = int(input())
a = list(map(int, input().split()))
move = [0] * (n+1)
a_dict = {}
for i in range(n):
    a_dict[a[i]] = i

for i in range(n-1):
    min_value = i+1
    min_idx = a_dict[min_value]

    if min_idx != i:
        a[i], a[min_idx] = a[min_idx], a[i]

        a_dict[a[min_idx]] = min_idx
        a_dict[a[i]] = i

        move[a[i]] += min_idx - i
        move[a[min_idx]] += min_idx - i

print(*move[1:])