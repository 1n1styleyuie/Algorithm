class Solution:
    def minOperations(self, logs: List[str]) -> int:
        cnt = 0

        for log in logs:
            # 상단 폴더로 가는 거지만 최상단일 경우는 건너뛰어야 한다.
            if log == "../":
                if cnt == 0:
                    continue
                else:
                    cnt -= 1
            # 같은 폴더 내부를 말하는걸로 건너뛰기
            elif log == "./":
                continue
            # 그 외에는 +1 하면 된다.
            else:
                cnt += 1
            
        return cnt  