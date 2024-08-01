def solution(arr):
    answer = []
    # 첫번째 숫자를 먼저 넣고 시작
    answer.append(arr[0])
    for i in range(1, len(arr)):
        # 이전숫자와 비교해서 다르면 현재숫자 저장
        if arr[i] != arr[i-1]:
            answer.append(arr[i])
    return answer