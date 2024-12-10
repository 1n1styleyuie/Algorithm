# 1654 s2
import sys
input = sys.stdin.readline

k, n = map(int, input().split())
nums = []
for _ in range(k):
    nums.append(int(input()))

start = 1
end = max(nums)

while start <= end:
    mid = (start + end) // 2
    # 카운트는 반복할때 마다 초기화
    cnt = 0

    # mid의 길이만큼 잘라내서 카운트
    for num in nums:
        cnt += num // mid
    
    if cnt >= n:
        start = mid + 1
    else:
        end = mid - 1

# 최대 길이 출력
print(end)