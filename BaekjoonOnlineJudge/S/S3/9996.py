# 9996 s3
import sys
input = sys.stdin.readline

'''
start와 end가 한글자가 아니라 긴 문자열일 수 있다.
start, end의 합이 주어진 문자열보다 길면 NE가 출력되어야 하고,
start를 비교하고 남은 문자열의 길이가 end보다 작으면 NE가 출력되어야 한다.
'''

n = int(input())
start, end = input().rstrip().split('*')
for _ in range(n):
    s = input().rstrip()
    if len(s) < len(start) + len(end):
        print('NE')
    elif s[:len(start)] == start and s[-len(end):] == end:
        print('DA')
    else:
        print('NE')