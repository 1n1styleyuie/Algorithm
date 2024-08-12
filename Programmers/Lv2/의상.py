def solution(clothes):
    
    clothes_dict = {}
    for a, b in clothes:
        # 이미 의상 종류가 있으면 추가
        if b in clothes_dict:
            clothes_dict[b].append(a)
        # 없으면 종류 생성하여 추가
        else:
            clothes_dict[b] = [a]
    
    
    answer = 1
    for i in clothes_dict:
        # 의상 수와 안입는 경우를 더한값을 answer에 곱하여 저장
        answer *= (len(clothes_dict[i])+1)
    # 아무것도 입지 않는 경우를 하나 빼서 return
    return answer-1