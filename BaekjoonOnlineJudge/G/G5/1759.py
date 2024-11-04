# 1759 g5
import sys
input = sys.stdin.readline
from itertools import combinations

L, C = map(int, input().split())

alphabets = input().split()

# 오름차순 정렬해서 combination
combi = combinations(sorted(alphabets), L)

res = []

for comb in combi:
    vowel = 0
    consonant = 0

    # 모음일 경우 vowel + 1
    # 자음일 경우 consonant + 1
    for a in comb:
        if a in 'aieou':
            vowel += 1
        else:
            consonant += 1
    
    # 모음이 1개 이상, 자음이 2개 이상일 경우에 출력
    if vowel >= 1 and consonant >= 2:
        print(''.join(comb))

