def solution(brown, yellow):
    answer = []
    w = brown + yellow
    h = 1
    while True:
        # 가로의 길이가 세로 길이와 같거나 길고
        # 전체 넓이가 주어진 값과 같으며
        # 노란색으로 칠해진 수가 일치할 경우
        # 가로-2, 세로-2는 갈색으로 테두리가 칠해지기 때문에 양쪽 2칸을 뺀 값을 곱함
        if w >= h and w*h == (brown+yellow) and (w-2)*(h-2) == yellow:
            answer.append(w)
            answer.append(h)
            break
        else:
            # 가로의 값을 줄여가면서 전체 넓이에 맞는 세로 값을 찾기
            while True:
                w -= 1
                if (brown+yellow) % w == 0:
                    h = (brown+yellow) // w
                    break
    return answer