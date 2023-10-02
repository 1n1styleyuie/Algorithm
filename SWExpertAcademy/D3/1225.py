import sys
sys.stdin = open('input.txt')

for tc in range(1, 11):
    test_case = int(input())
    pwd_list = list(map(int, input().split()))
    minus_cnt = 1 # 감소할 숫자를 나타내기 위해 변수 설정
    while True:
        num1 = pwd_list.pop(0) # 맨 앞 숫자 pop
        if minus_cnt == 1: # 카운트가 1이면 pop한 값에서 -1하고 다시 저장
            pwd_list.append(num1 -1)
            minus_cnt += 1 # 1을 뺀 다음은 2를 빼야하기 때문에 +1
        elif minus_cnt == 2: # 카운트가 2이면 pop한 값에서 -2하고 다시 저장
            pwd_list.append(num1 -2)
            minus_cnt += 1 # 2를 뺀 다음은 3을 빼야하기 때문에 +1
        elif minus_cnt == 3: # 카운트가 3이면 pop한 값에서 -3하고 다시 저장
            pwd_list.append(num1 - 3)
            minus_cnt += 1 # 3을 뺀 다음은 4를 빼야하기 때문에 +1
        elif minus_cnt == 4: # 카운트가 4이면 pop한 값에서 -4하고 다시 저장
            pwd_list.append(num1 - 4)
            minus_cnt += 1 # 4를 뺀 다음은 5를 빼야하기 때문에 +1
        elif minus_cnt == 5: # 카운트가 5이면 pop한 값에서 -5하고 다시 저장
            pwd_list.append(num1 - 5)
            minus_cnt = 1 # 다시 초기값으로 돌리기 위해 1로 바꿔줌

        # 종료조건이 0보다 작아지거나 0일경우
        if pwd_list[-1] == 0 or pwd_list[-1] < 0:
            # 마지막 값은 0으로 저장되며 해당 숫자 배열이 암호가 된다.
            pwd_list[-1] = 0
            # 따라서 마지막이 0이기 때문에 while 탈출
            break

    print(f'#{tc}', *pwd_list)