# 7662 g4
import sys
input = sys.stdin.readline
import heapq

def empty(nums):
    for num in nums:
        if num[1] > 0:
            return False
    return True


t = int(input())
for _ in range(t):
    k = int(input())
    min_heap = []
    max_heap = []
    nums = {}
    for _ in range(k):
        s, n = input().rstrip().split()
        n = int(n)
        if s == 'I':
            if n in nums:
                nums[n] += 1
            else:
                # 파이썬에서 지원하는 힙의 경우 최소힙을 지원하기 때문에 최대힙을 위해서 음수 부호를 붙인다.
                nums[n] = 1
                heapq.heappush(min_heap, n)
                heapq.heappush(max_heap, -n)
        
        elif s == 'D':
            if not empty(nums.items()):
                # 이미 삭제된 데이터인 경우 지워줘야 한다.
                if n == 1:
                    while -max_heap[0] not in nums or nums[-max_heap[0]] < 1:
                        tmp = -heapq.heappop(max_heap)
                        if tmp in nums:
                            del(nums[tmp])
                    nums[-max_heap[0]] -= 1
                else:
                    while min_heap[0] not in nums or nums[min_heap[0]] < 1:
                        tmp = heapq.heappop(min_heap)
                        if tmp in nums:
                            del(nums[tmp])
                    nums[min_heap[0]] -= 1

    if empty(nums.items()):
        print('EMPTY')
    else:
        while -max_heap[0] not in nums or nums[-max_heap[0]] < 1:
            heapq.heappop(max_heap)
        while min_heap[0] not in nums or nums[min_heap[0]] < 1:
            heapq.heappop(min_heap)
        print(-max_heap[0], min_heap[0])