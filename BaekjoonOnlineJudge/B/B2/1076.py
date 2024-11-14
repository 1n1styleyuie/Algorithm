# 1076 b2
import sys
input = sys.stdin.readline

res = ''
color = {'black' : ['0', 1], 'brown' : ['1', 10], 'red' : ['2', 100], 'orange' : ['3', 1000],
        'yellow' : ['4', 10000], 'green' : ['5', 100000], 'blue' : ['6', 1000000], 
        'violet' : ['7', 10000000], 'grey' : ['8', 100000000], 'white' : ['9', 1000000000]}
for i in range(3):
    c = input().rstrip()
    if i == 2:
        print(int(res) * color[c][1])
    else:
        res += color[c][0]