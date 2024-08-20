def solution(people, limit):
    answer = 0
    people.sort()
    start = 0
    end = len(people) - 1
    while start <= end:
        # 두명이 탑승가능하면 start + 1, end - 1 
        if people[end] + people[start] <= limit:
            start += 1
            end -= 1
        # 그 외 경우 end - 1
        else:
            end -= 1
        # answer에 카운트
        answer += 1
    return answer