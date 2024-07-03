class Solution:
    def minDifference(self, nums: List[int]) -> int:
        # 4개 이하면 결국 3개가 바뀌는데 값이 다 같아지니까 0
        if len(nums) <= 4:
            return 0

        nums.sort()

        answer = float("inf")

        # 앞에 세개를 바꾸거나 뒤 세개를 바꾸는 경우일 때 가장 작은값을 저장하는 방식으로
        # 결국엔 중간에 있는 값들은 남아 있게 되니까
        for l in range(4):
            r = len(nums) - 4 + l
            answer = min(answer, nums[r] - nums[l])

        return answer