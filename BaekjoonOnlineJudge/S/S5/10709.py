# 10709 s5
import sys
input = sys.stdin.readline

h, w = map(int, input().split())
arr = [list(input().rstrip()) for _ in range(h)]
ans = [[-1] * w for _ in range(h)]
for i in range(h):
    # cnt는 매 줄마다 초기화
    cnt = 0
    for j in range(w):
        # 구름을 만났다면 해당 지역은 0
        # cnt를 1로 초기화
        if arr[i][j] == 'c':
            ans[i][j] = 0
            cnt = 1
        else:
            # 구름이 이전에 있었다면
            if cnt:
                # 시간만큼 저장하고
                # cnt + 1
                ans[i][j] = cnt
                cnt += 1
            else:
                # 아닐경우 그 전에 구름이 없기 때문에 -1 저장
                ans[i][j] = -1
            

for i in range(h):
    print(*ans[i])