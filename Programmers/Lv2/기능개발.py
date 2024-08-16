from collections import deque
def solution(progresses, speeds):
    answer = []
    progresses = deque(progresses)
    speeds = deque(speeds)
    time = 1
    cnt = 0
    while progresses:
        # 작업 진도 + 시간 * 작업 속도 가 100을 넘을 경우 cnt + 1 한 후 현재 작업 진도, 작업속도를 pop
        if (progresses[0]+speeds[0]*time) >= 100:
            progresses.popleft()
            speeds.popleft()
            cnt += 1
        else:
            # cnt가 있었을 경우 answer에 저장하고 0으로 초기화
            if cnt:
                answer.append(cnt)
                cnt = 0
            # 그 외 경우 시간 + 1
            else:
                time += 1
    answer.append(cnt)
    return answer