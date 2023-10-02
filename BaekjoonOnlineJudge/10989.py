import sys
input = sys.stdin.readline

N = int(input())
# 1 <= num <= 10000
nums_arr = [0]*10001
for i in range(N):
    num = int(input())
    # 입력된 숫자 인덱스에 +1 해서 카운트
    nums_arr[num] += 1

# 모든 인덱스에 대해
for k in range(10001):
    # 값이 있다면
    if nums_arr[k] != 0:
        # 인덱스에 계산된 숫자만큼 해당 인덱스 숫자 출력
        for ls in range(nums_arr[k]):
            print(k)