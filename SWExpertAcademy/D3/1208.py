for test_case in range(1, 11):
    # ///////////////////////////////////////////////////////////////////////////////////
    dump = int(input())
    box = list(map(int, input().split()))
    for n in range(dump): # dump 횟수만큼 반복
        for i in range(len(box)-1, 0, -1): # Bubble sort
            for j in range(0, i):
                if box[j] > box[j + 1]:
                    box[j], box[j + 1] = box[j + 1], box[j]
        box[-1] -= 1 # 가장 큰값에서 -1
        box[0] += 1 # 가장 작은값에서 +1
        if box[-1] - box[0] <= 1: # 큰값과 작은값의 차가 1이하일 경우 break
            print(f'#{test_case} {box[-1] - box[0]}')
            break
    for i in range(len(box)-1, 0, -1): # dump가 끝난뒤 정렬이 되지 않은 리스트를 다시 정렬
        for j in range(0, i):
            if box[j] > box[j + 1]:
                box[j], box[j + 1] = box[j + 1], box[j]
    print(f'#{test_case} {box[-1] - box[0]}')