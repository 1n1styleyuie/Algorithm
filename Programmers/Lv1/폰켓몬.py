def solution(nums):
    answer = 0
    s = len(set(nums))
    # set으로 만든 배열의 길이가 원래 길이보다 클 경우
    # answer 은 전체 배열 길이에서 // 2 한 값으로 리턴한다.
    if s >= (len(nums)//2):
        answer = len(nums) // 2
    # 그 외 경우 set으로 만든 배열의 길이를 리턴한다.
    else:
        answer = s
    return answer