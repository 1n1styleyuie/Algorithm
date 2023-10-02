import sys
sys.stdin = open('input.txt', 'r')
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]
    max_v = 0 # 모든 원소가 0이상이라면
    for i in range(N): # 모든 원소 arr[i][j]에 대해
        for j in range(M):
            # arr[i][j]를 중심으로
            s = arr[i][j]
            count = 0
            count += s
            for k in range(4):
                ni, nj = i+di[k], j+dj[k]
                if 0 <= ni < N and 0 <= nj < M: # 배열을 벗어나지 않으면
                    count += arr[ni][nj]
            if max_v < count:
                max_v = count
    print(f'#{tc} {max_v}')