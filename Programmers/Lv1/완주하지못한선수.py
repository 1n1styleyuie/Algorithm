def solution(participant, completion):
    a = {}
    # 딕셔너리에 참가자 저장
    for p in participant:
        if p in a:
            a[p] += 1
        else:
            a[p] = 1
    # 완주한 사람들을 딕셔너리에 저장되어있는 목록에서 제거
    for c in completion:
        a[c] -= 1

    # 단 한명만 완주를 못했기 때문에 1인 값을 찾아서 리턴
    for i in a:
        if a[i] == 1:
            return i
    

