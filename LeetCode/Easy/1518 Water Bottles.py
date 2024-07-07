class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        answer = 0
        answer += numBottles
        emt = numBottles
        while (emt // numExchange):
            answer += (emt//numExchange)
            emt = (emt//numExchange) + (emt%numExchange)
        return answer