# 1629 s1
import sys
input = sys.stdin.readline

'''
내장 함수 pow란
pow(base, exp, mod=None)
base는 밑, exp는 지수, mod는 나머지 계산을 할 떄 이용한다.
따라서 밑과 지수를 넣으면 자동으로 base ** exp 값이 계산되며
mod를 넣어 해당 값을 넣었을 때 나머지를 구할 수 있다.

이 문제에서 a의 b제곱을 한 후 c로 나눈 나머지를 구하는 문제이기 떄문에
pow(a, b, c) 를 구하면 나머지가 출력된다.

Python 내장함수는 신이고 무적이다.
'''

a, b, c = map(int, input().split())
print(pow(a, b, c))