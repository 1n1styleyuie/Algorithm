import sys
input = sys.stdin.readline

n = int(input())
total = 0
nums = {}
arr = []
for _ in range(n):
    num = int(input())
    if num in nums:
        nums[num] += 1
    else:
        nums[num] = 1
    arr.append(num)
    total += num
arr.sort()
# value의 내림차순, key의 오름차순으로 정렬
nums = sorted(nums.items(), key=lambda x : (-x[1], x[0]))

# 산술평균
print(round(total/n))
# 중앙값
print(arr[n//2])

# 최빈값
# n = 1일 경우 해당 값을 바로 출력
if n == 1:
    print(nums[0][0])
else:
    # 만약 여러개일 경우 최빈값 중 두번째로 작은값 출력
    if nums[0][1] == nums[1][1]:
        print(nums[1][0])
    else:
        print(nums[0][0])

# 둘다 0 미만인 경우 
if arr[0] < 0 and arr[-1] < 0:
    print(abs(arr[0]) + arr[-1])
# 제일 작은 값이 0 미만인 경우
elif arr[0] < 0:
    print(abs(arr[0]) + arr[-1])
# 둘다 0 이상인 경우
else:
    print(arr[-1] - arr[0])
