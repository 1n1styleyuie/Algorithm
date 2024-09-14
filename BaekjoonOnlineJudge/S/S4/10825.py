# 10825 s4

import sys
input = sys.stdin.readline

n = int(input())
arr = [list(input().rstrip().split()) for _ in range(n)]

'''
정렬 조건에 맞추어 정렬
1. 국어 점수 내림차순
2. 국어 점수 같을 경우 영어 점수 오름차순
3. 국어, 영어 점수 같을 경우 수학 점수 내림차순
4. 모든 점수 같을 경우 이름 오름차순
'''

arr.sort(key=lambda x : (-int(x[1]), int(x[2]), -int(x[3]), x[0]))

for a in arr:
    print(a[0])