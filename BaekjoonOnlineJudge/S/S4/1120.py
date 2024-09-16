# 1120 s4
import sys
input = sys.stdin.readline


a, b = input().split()

min_cnt = 10**6

'''
adaabc aababbc
A가 B보다 작거나 같기 떄문에 i의 범위를 len(b)-len(a)+1로 하여 0과 1일 경우 탐색을 하게 된다.
그 경우 j에 대하여 반복을 할 때
i가 0일 경우 a = adaabc, b = aababb 일 경우 탐색하여 카운트 하고
i가 1일 경우 a = adaabc, b = ababbc 로 탐색을 하게 된다.
따라서 이 중 최소로 하는 경우를 min_cnt에 저장하여 출력하면 된다.
'''

for i in range(len(b)-len(a)+1):
    cnt = 0 
    for j in range(len(a)):
        if a[j] != b[i+j]:
            cnt += 1
    min_cnt = min(min_cnt, cnt)

print(min_cnt)