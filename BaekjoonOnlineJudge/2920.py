num1_lst = list(map(int, input().split()))

if num1_lst == sorted(num1_lst):
    print('ascending')
elif num1_lst == sorted(num1_lst, reverse=True):
    print('descending')
else:
    print('mixed')