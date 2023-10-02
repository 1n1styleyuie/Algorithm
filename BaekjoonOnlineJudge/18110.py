import sys
input = sys.stdin.readline

def f(num):
    if num - int(num) >= 0.5:
        return int(num)+1
    else:
        return int(num)


N = int(input())
if N == 0:
    print(0)
else:
    arr = [int(input()) for _ in range(N)]
    minus_people = f(N * 0.15)
    arr.sort()
    if minus_people:
        print(f(sum(arr[minus_people:-minus_people])/(N-2*minus_people)))
    else:
        print(f(sum(arr)/(N-2*minus_people)))