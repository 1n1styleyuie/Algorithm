class Solution:
    def passThePillow(self, n: int, time: int) -> int:

        # full이 홀수이면 편도, 짝수이면 왕복
        full = time // (n - 1)

        # extra는 full로 이동하는 것에서 추가로 이동하는 거리를 미리 계산
        extra = time % (n - 1)

        # 왕복으로 갔다오고 extra가 남아있는 경우
        # extra는 추가 이동 거리이기 때문에 +1하여 return
        if full % 2 == 0:
            return extra + 1
        # 편도로 갔다가 남은 extra가 있기 때문에
        # 마지막 번호인 n에서 extra만큼 이동한 번호를 return
        else:
            return n - extra
