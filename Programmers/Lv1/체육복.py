def solution(n, lost, reserve):
    answer = 0
    # 인덱스로 찾기 위해 student[0] = 0으로 저장하고 나머지를 1로 저장
    student = [0] + [1] * n
    # 여벌 체육복 있는 학생에 +1
    for r in reserve:
        student[r] += 1
    # 도난당한 학생에 -1
    for l in lost:
        student[l] -= 1

    for i in range(1, n+1):
        # 체육복이 없을 때
        if student[i] == 0:
            # 앞 번호가 여벌이 있을 경우
            if i > 1 and student[i-1] > 1:
                student[i] += 1
                student[i-1] -= 1
                continue
            # 뒷 번호가 여벌이 있을 경우
            if i < n and student[i+1] > 1:
                student[i] += 1
                student[i+1] -= 1
                continue

    # 체육복이 있는 경우를 확인해서 answer에 저장
    for j in range(len(student)):
        if student[j] >= 1:
            answer += 1

    return answer