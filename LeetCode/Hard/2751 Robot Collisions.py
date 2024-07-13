from collections import deque

class Solution:
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
        lst = list(range(len(positions)))
        result = []
        q = deque()

        # lst는 positions에 섞여있는 위치들을 idx로 순서를 표기하기 위해 람다를 통해 정렬
        # idx를 lst에서 꺼내게 되면 해당 idx를 postion[idx]에서 찾으면 가장 위치가 앞인 순서부터 찾아진다.
        lst.sort(key = lambda x: positions[x])
        for idx in lst:
            # 우측인것만 저장
            if directions[idx] == 'R':
                q.append(idx)
            else:
                while q and healths[idx] > 0:
                    top_idx = q.pop()
                    if healths[top_idx] > healths[idx]:
                        healths[top_idx] -= 1
                        healths[idx] = 0
                        q.append(top_idx)
                    elif healths[top_idx] < healths[idx]:
                        healths[idx] -= 1
                        healths[top_idx] = 0
                    else:
                        healths[idx] = 0
                        healths[top_idx] = 0
        
        for i in range(len(positions)):
            if healths[i] > 0:
                result.append(healths[i])

        return result