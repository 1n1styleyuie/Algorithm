import sys
input = sys.stdin.readline

t = int(input())
for tc in range(t):
    a, b = input().split()
    a = int(a)
    print(b[:(a-1)]+b[a:])