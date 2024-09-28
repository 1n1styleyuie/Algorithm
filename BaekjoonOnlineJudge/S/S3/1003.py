# s3 1003
import sys
input = sys.stdin.readline


t = int(input())
for _ in range(t):
    n = int(input())
    
    # 40보다 작거나 같은 수 이기 때문에 41개 배열 생성
    zero = [0] * 41
    one = [0] * 41

    # 피보나치 수열이 0과 1일 경우의 값을 미리 저장
    zero[0], one[0] = 1, 0
    zero[1], one[1] = 0, 1

    for i in range(2, n+1):
        zero[i] = zero[i-1] + zero[i-2]
        one[i] = one[i-1] + one[i-2]

    print(zero[n], one[n])