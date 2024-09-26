# 17626 s3
import sys
input = sys.stdin.readline
import math

def f(n):
    # 한개의 제곱수만으로 표현이 가능한 경우
    # 루트를 씌운 값이 같다면 1
    if int(math.sqrt(n)) == math.sqrt(n):
        return 1
    
    # 두개의 제곱수로 표현이 가능한 경우
    # √(n - i^2)이 같을 경우 2
    for i in range(1, int(math.sqrt(n)) + 1):
        if int(math.sqrt(n - i**2)) == math.sqrt(n - i**2):
            return 2
    
    # 세개의 제곱수로 표현이 가능한 경우
    # √(n - i^2 - j^2)이 같을 경우 3
    for i in range(1, int(math.sqrt(n)) + 1):
        for j in range(1, int(math.sqrt(n - i**2)) + 1):
            if int(math.sqrt(n - i**2 - j**2)) == math.sqrt(n - i**2 - j**2):
                return 3
    
    # 네개의 제곱수로 모두 표현이 가능하기 때문에 세개의 제곱수로 표현되지 않을 경우 4 리턴
    return 4


n = int(input())
print(f(n))
