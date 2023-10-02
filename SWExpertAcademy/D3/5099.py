T = int(input())
for tc in range(1, T+1):
    # N : 화덕의 크기, M : 피자 개수
    N, M = map(int, input().split())
    # 피자 치즈의 양을 리스트로 입력받음
    num_pizza = list(map(int, input().split()))
    # 화덕 큐 생성
    fire_pot = []
    # 인덱스를 추가해주기 위해 번호 리스트 생성
    idx = [i for i in range(1, M+1)]
    # 반복문을 통해서 튜플 형태로 화덕 큐에 추가
    for i in range(1, N+1):
        # (피자 번호, 피자 치즈 양) 순으로 추가
        fire_pot.append((idx.pop(0), num_pizza.pop(0)))
    # 카운트 변수 생성
    cnt = 0
    # 인덱스 번호를 저장하기 위한 변수 생성
    v = 0
    while True:
        # 카운트가 피자 개수와 같다는 것은 모든 피자가
        # 조리가 완료되어 끝났다는 조건이므로 while문 종료
        if cnt == M:
            break
        # v : 피자 번호, c : 피자 치즈 양
        v, c = fire_pot.pop(0)
        # 피자 치즈 양 // 2를 m 에 저장
        m = c // 2
        # 만약 피자 치즈 양이 0이라면
        if m == 0:
            # 피자가 아직 남아있다면
            if num_pizza:
                # 화덕에 추가하기 위해
                # 피자 치즈 리스트에서 pop
                m = num_pizza.pop(0)
                # 피자 번호 리스트에서 pop
                v = idx.pop(0)
                # 피자 한판이 조리가 되어 나간 것이기 때문에
                # 조리된 피자의 수 1 추가
                cnt += 1
                # 피자 번호와 피자 치즈 양을 화덕에 추가
                fire_pot.append((v, m))
            # 더이상 조리할 피자가 리스트에 존재하지 않기때문에
            # 조리된 피자의 수만 1 추가
            else:
                cnt += 1
        # 그 외 조건에서는 조리가 아직 덜 된것이기 때문에
        # 다시 화덕에 집어 넣으면 된다.
        else:
            fire_pot.append((v, m))
    # 마지막으로 조리된 피자의 번호가 v에 이미 저장되어 있기 때문에
    # v를 출력하면 마지막에 조리된 피자 번호가 나오게 된다.
    print(f'#{tc} {v}')
