T = int(input())  # testcase
for tc in range(1, T+1):
    N = int(input())  # 자연수의 개수
    numbers = list(map(int, input().split()))  # 자연수들

# 준비작업
    heap = [0] * (N+1)  # N+1 개 배열 생성
    last = 0

# 완전 이진 트리 유지
    for num in numbers:
        last += 1  # 현재 노드 위치
        heap[last] = num  # 노드에 추가
# 최소 힙 만족하는지 확인
        c = last  # 자식 노드 = 현재 노드
        p = last // 2  # 현재 노드의 부모 노드
        while p > 0 and heap[p] > heap[c]:  # 부모 있고 부모>자식의 경우
            heap[p], heap[c] = heap[c], heap[p]  # 위치 교환
            c = p  # 부모를 새로운 자식 노드로
            p = c // 2  # 부모 노드를 계산


# 조상 노드 찾고 -> 숫자 더하기
    ancestor_nodes = 0  # 조상노드들의 합
    p_last = last // 2  # last의 부모 노드

    while p_last > 0:  # 부모 노드가 있을 때까지
        ancestor_nodes += heap[p_last]  # 부모 노드 더하기
        p_last = p_last // 2  # 조상 찾아 올라가기

    print(f'#{tc}', ancestor_nodes)