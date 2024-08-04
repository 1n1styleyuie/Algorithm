def solution(array, commands):
    answer = []
    # i, j, k에 대해서
    for i, j, k in commands:
        # i-1 에서 j까지 슬라이싱으로 lst에 저장 후 정렬
        lst = array[i-1:j]
        lst.sort()
        # k-1번째 숫자를 answer에 저장
        answer.append(lst[k-1])
    return answer