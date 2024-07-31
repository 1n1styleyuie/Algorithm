def solution(sizes):
    answer = 0
    max_w = 0
    max_h = 0
    for size in sizes:
        # 세로길이가 길면 가로랑 바꿔준다.
        if size[0] < size[1]:
            temp = size[0]
            size[0] = size[1]
            size[1] = temp
        # 큰값들을 저장
        max_w = max(max_w, size[0])
        max_h = max(max_h, size[1])
    
    answer = max_w * max_h
    return answer