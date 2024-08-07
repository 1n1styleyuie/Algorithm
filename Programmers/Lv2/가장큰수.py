def solution(numbers):
    # 문자열 형태로 저장
    n = list(map(str, numbers))
    # 정렬을 할 때 x*3의 값을 key로
    # 이는 numbers의 원소가 1000이하이기 떄문
    n.sort(key = lambda x : x * 3, reverse = True)
    return str(int(''.join(n)))