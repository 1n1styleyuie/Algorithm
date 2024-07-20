class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        n = len(rowSum)
        m = len(colSum)
        
        # 결과값을 저장할 리스트
        res = [[0] * m for _ in range(n)]

        # 행과 열 합 중에서 작은 값을 넣고 그 값을 행과 열 합에서 빼준다.
        for i in range(n):
            for j in range(m):
                res[i][j] = min(rowSum[i], colSum[j])
                rowSum[i] -= res[i][j]
                colSum[j] -= res[i][j]

        return res