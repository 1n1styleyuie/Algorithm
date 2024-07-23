from collections import defaultdict

class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        res = []
        # 내림차순
        nums.sort(reverse=True)
        
        num_dict = defaultdict(int)

        for num in nums:
            num_dict[num] += 1
        
        # 카운트 순으로 정렬
        num_dict = sorted(num_dict.items(), key = lambda x : x[1])
        
        for num in num_dict:
            for _ in range(num[1]):
                res.append(num[0])

        return res