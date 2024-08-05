def solution(answers):
    answer = []
    # 찍는 방식
    a = [1, 2, 3, 4, 5]
    b = [2, 1, 2, 3, 2, 4, 2, 5]
    c = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    a_cnt = 0
    b_cnt = 0
    c_cnt = 0
    
    # i를 찍는방식의 길이의 나머지로 계산을 하면 찍는 방식을 반복으로 돌리면서 계산이 가능하다.
    for i in range(len(answers)):
        if a[i%len(a)] == answers[i]:
            a_cnt += 1
        if b[i%len(b)] == answers[i]:
            b_cnt += 1
        if c[i%len(c)] == answers[i]:
            c_cnt += 1
            
    # 가장 큰값을 찾고 그 값이 어떤 값인지 찾아서 answer에 저장        
    max_cnt = max(a_cnt, b_cnt, c_cnt)
    if max_cnt == a_cnt:
        answer.append(1)
    if max_cnt == b_cnt:
        answer.append(2)
    if max_cnt == c_cnt:
        answer.append(3)
    return answer