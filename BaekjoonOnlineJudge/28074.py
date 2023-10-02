import sys
input = sys.stdin.readline
# 28074
str1 = input()
check = ['M', 'O', 'B', 'I', 'S']
result = True
for i in check:
    if i not in str1:
        result = False
        break

if result:
    print('YES')
else:
    print('NO')