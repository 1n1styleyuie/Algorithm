#7785
import sys
input = sys.stdin.readline
n = int(input())
logs = {}

for _ in range(n):
    name, log = map(str, input().split())
    if log == 'enter':
        logs[name] = log
    else:
        del logs[name]

logs = sorted(logs.keys(), reverse=True)

for i in logs:
    print(i)