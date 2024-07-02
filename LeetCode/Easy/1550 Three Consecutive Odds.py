class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        cnt = 0
        for i in range(len(arr)):
            if arr[i] % 2 == 1:
                cnt += 1
            else:
                cnt = 0

            if cnt == 3:
                return True