class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        lst = []
        for i in range(len(names)):
            lst.append([names[i], heights[i]])
        lst.sort(reverse = True, key = lambda x: x[1])
        res = []
        for i in range(len(names)):
            res.append(lst[i][0])
        return res