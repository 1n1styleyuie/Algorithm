# 7662 g4
import sys
input = sys.stdin.readline

m, n = map(int, input().split())

'''
에라토스테네스의 체란 소수를 대량으로 빠르게 찾는 알고리즘이다.
16의 경우 1, 2, 4, 8, 16의 약수를 갖고 16의 양의 제곱근인 4를 기준으로 대칭을 이룬다. 
16이 2로 나누어 떨어짐을 알게된다면 8로 나누어 떨어지는 것은 자동적으로 참이 된다.

따라서 이 문제에서 i가 소수임을 판단하기 위해서는 2부터 i의 제곱근까지 나누어 떨어지는지만 확인하면 된다.
이 경우 시간복잡도는 루트n 이 된다.
'''

for i in range(m, n+1):
    if i < 2:
        continue

    for j in range(2, int(i**0.5)+1):
        if i % j == 0:
            break
    else:
        print(i)