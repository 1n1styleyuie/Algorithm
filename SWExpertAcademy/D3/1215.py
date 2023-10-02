import sys
sys.stdin = open('input.txt')

for tc in range(1, 11):
    N = int(input())
    arr = [input() for _ in range(8)]

    cnt = 0
    for i in range(8):
        for j in range(8-N+1):
            for k in range(N//2):
                if arr[i][j+k] != arr[i][j+N-1-k]:
                    break
            else:
                cnt += 1
            for k in range(N//2):
                if arr[j+k][i] != arr[j+N-1-k][i]:
                    break
            else:
                cnt += 1
    print(f'#{tc} {cnt}')