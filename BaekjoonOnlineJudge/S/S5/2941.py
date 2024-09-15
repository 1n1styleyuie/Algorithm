# 2941 s5

import sys
input = sys.stdin.readline

s = input().rstrip()

croatia = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

# 크로아티아 단어를 'i'로 바꿔서 길이를 구하면 쉽게 해결할 수 있다.
for c in croatia:
    s = s.replace(c, 'i')

print(len(s))