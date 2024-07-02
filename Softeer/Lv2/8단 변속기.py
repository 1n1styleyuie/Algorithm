import sys


asc = ['1', '2', '3', '4', '5', '6', '7', '8']
des = ['8', '7', '6', '5', '4', '3', '2', '1']

dct = list(input().split())

if dct == asc:
    print('ascending')
elif dct == des:
    print('descending')
else:
    print('mixed')