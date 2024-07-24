class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        maps = []
        
        for i in range(len(nums)):
            str_num = str(nums[i])
            # 매핑된 번호를 저장하기 위한 문자열
            mapping_num = ''

            for j in range(len(str_num)):
                # 매핑된 번호를 문자열에 더함
                mapping_num += str(mapping[int(str_num[j])])
            # 저장된 문자열을 maps에 인덱스와 같이 저장
            maps.append((int(mapping_num), i))
    
        maps.sort()
        res = []
        # 인덱스 번호 순서대로 res에 저장하여 return
        for m in maps:
            res.append(nums[m[1]])
        print(res)
        return res