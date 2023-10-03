import sys
input = sys.stdin.readline

# 10101
num = []
for _ in range(3):
    num.append(int(input()))

if num[0] == 60 and num[1] == 60 and num[2] == 60:
    print('Equilateral')
elif sum(num) == 180 and (num[0] == num[1] or num[0] == num[2] or num[1] == num[2]):
    print('Isosceles')
elif sum(num) == 180 and (num[0] != num[1] or num[0] != num[2] or num[1] != num[2]):
    print('Scalene')
elif sum(num) != 180:
    print('Error')