# s5 7568
import sys
input = sys.stdin.readline


n = int(input())
arr = []

for _ in range(n):
    x, y = map(int, input().split())
    arr.append([x, y])

'''
덩치 등수를 구할 때 키와 몸무게가 모두 커야만 그 사람보다 덩치가 크다고 말할 수 있다.
따라서 이중 반복을 통해 비교하여 rank를 계산한다.

N명의 집단에서 각 사람의 덩치 등수는 자신보다 더 "큰 덩치"의 사람의 수로 정해진다. 
만일 자신보다 더 큰 덩치의 사람이 k명이라면 그 사람의 덩치 등수는 k+1이 된다.

5
55 185
58 183
88 186
60 175
46 155
예시가 주어졌을 경우
A의 경우 자신보다 큰 경우는 88 186인 C 한명이다. 따라서 자신보다 덩치가 큰 사람이 1명이므로 A의 덩치 등수는 2이다.
B의 경우도 자신보다 큰 경우는 C 한명이므로 2등이다.
C는 자신보다 덩치가 큰 사람이 없기 떄문에 1등이다.
D도 자신보다 큰 경우는 C 한명이므로 2등이다.
E는 자신보다 덩치가 큰 사람이 4명이 있기 때문에 5등이 된다.
'''
for a in arr:
    rank = 1
    for b in arr:
        if a[0] < b[0] and a[1] < b[1]:
            rank += 1    
    print(rank, end=" ")