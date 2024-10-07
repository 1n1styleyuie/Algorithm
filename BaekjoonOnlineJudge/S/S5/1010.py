# 1010 s5
import sys
input = sys.stdin.readline
import math

'''
combination(조합)은 from itertools import combination으로 사용한다.
combination(arr, number)로 배열과 숫자를 넣게 되면 
배열에 있는 값들을 number만큼 뽑아서 하나의 배열로 생성하게 된다.

하지만 이 문제에서는 일반적인 조합을 구하는 수식으로 풀면 된다.
n <= m 인 상태에서
m개의 도시가 n개의 다리를 만든다고 생각하면
mCn  조합으로 표현된다.
따라서 이 문제에서는 조합을 계산하는

m! // (n!(m-n)!)

으로 계산하여 출력한다.
'''


t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    res = math.factorial(m) // (math.factorial(n) * math.factorial(m-n))
    print(res) 