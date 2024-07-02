class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        answer = []

        nums1set = set(nums1)
        nums2set = set(nums2)

        numsintersection = nums1set.intersection(nums2set)

        for i in numsintersection:
            mincount=min(nums1.count(i), nums2.count(i))
            answer.extend([i]*mincount)

        return answer