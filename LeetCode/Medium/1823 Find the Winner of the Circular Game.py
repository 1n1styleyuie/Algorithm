from collections import deque


class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        q = deque()
        for i in range(1, n+1):
            q.append(i)
        
        while len(q) > 1:
            for j in range(k):
                if j+1 == k:
                    q.popleft()
                else:
                    q.append(q.popleft())
        answer = q.pop()
        return answer