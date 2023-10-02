def back_track(k):
    global ans
    val = int(''.join(cards))
    if val in visited[k]:
        return
    visited[k].add(val)
    if k == cnt:
        ans = max(ans, val)
    else:
        for i in range(num-1): # 교환할 왼쪽 카드
            for j in range(i+1, num): # 교환할 오른쪽 카드
                cards[i], cards[j] = cards[j], cards[i] # 교환
                back_track(k+1) # 교환횟수 1 늘려서 진행
                cards[i], cards[j] = cards[j], cards[i] # 원복


T = int(input())
for tc in range(1, T+1):
    ans = 0
    arr = list(input().split())
    cards, cnt = list(arr[0]), int(arr[1])
    num = len(cards)
    visited = [set() for _ in range(11)] # 최대 10회 교환
    back_track(0)
    print(f'#{tc} {ans}')
