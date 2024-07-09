class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        # waiting : 대기시간 총합
        waiting = 0
        # time : 현재까지 진행된 시간

        # 둘다 처음 들어오는 값은 먼저 계산하여 저장하고 시작한다.
        time = customers[0][0] + customers[0][1]
        waiting += (time - customers[0][0])

        for i in range(1, len(customers)):
            # 도착한 시간이 현재 시간보다 이후일 경우
            if customers[i][0] > time:
                # 그 시간에서 걸리는 시간을 더한게 현재 시간이 된다. 
                # 그러므로 time을 더하는게 아닌 다시 정의하면된다.
                time = customers[i][0] + customers[i][1]
                waiting += (time - customers[i][0])
            else:
                # 그 외는 도착한시간이 현재시간보다 작거나 같을 경우로 이후 진행 시간을 더해주면 된다.
                time += customers[i][1]
                waiting += (time - customers[i][0])

        return waiting / len(customers)