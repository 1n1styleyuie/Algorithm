import sys
N = int(sys.stdin.readline())

for _ in range(N):
    cnt, word = sys.stdin.readline().split()
    for x in word:
        print(x * int(cnt), end='')
    print()