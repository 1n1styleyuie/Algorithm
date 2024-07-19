class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        m = len(matrix)
        n = len(matrix[0])
        

        x_min_max = 0
        for i in range(m):
            x_min = min(matrix[i])
            x_min_max = max(x_min_max, x_min)

        y_max_min = 10**6
        for j in range(n):
            y_max = 0
            for i in range(m):
                if y_max < matrix[i][j]:
                    y_max = matrix[i][j]
            y_max_min = min(y_max_min, y_max)
            
        if x_min_max == y_max_min:
            return [x_min_max]
        else:
            return []
        