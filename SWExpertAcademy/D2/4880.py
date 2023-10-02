def match(start, end):
    if start == end:
        return start
    center = (start+end) // 2
    left = match(start, center) # 왼쪽 구간에서의 최종 승자
    right = match(center+1, end) # 오른쪽 구간에서의 최종 승자
    # p[left]  왼쪽 구간 승자의 카드
    # p[right]  오른쪽 구간 승자의 카드
    # left, right의 승패를 결정하고 이긴 쪽을 리턴
    winner = (p[left] - p[right]) % 3
    if winner == 2:
        return right
    else:
        return left


T = int(input())
for tc in range(1, T+1):
    n = int(input())
    p = list(map(int, input().split())) # player별 카드 저장
    print(f'#{tc}', match(0, n-1)+1) # 구간에서 승자의 인덱스를 리턴