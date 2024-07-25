class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        return self.merge_sort(nums)
    
    def merge_sort(self, lst):
        # 길이가 1인 경우 이미 정렬된 상태
        if len(lst) < 2:
            return lst
        
        # 중간점을 찾아서 분할 정렬
        mid = len(lst) // 2
        low_lst = self.merge_sort(lst[:mid])
        high_lst = self.merge_sort(lst[mid:])

        merged_lst = []
        l = h = 0
        # 숫자를 비교하여 리스트에 정렬된 순서로 추가
        while l < len(low_lst) and h < len(high_lst):
            if low_lst[l] < high_lst[h]:
                merged_lst.append(low_lst[l])
                l += 1
            else:
                merged_lst.append(high_lst[h])
                h += 1
        
        # 남은 숫자가 있다면 리스트에 추가
        merged_lst += low_lst[l:]
        merged_lst += high_lst[h:]
        return merged_lst
