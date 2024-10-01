# 18111 s2 (pypy제출)
import sys
input = sys.stdin.readline

n, m, b = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

res = 10**8
idx = 0

# 최대 높이는 256
for i in range(257):
    # remove는 제거할 블록 수, put은 놓아야할 블록 수
    remove, put = 0, 0

    for x in range(n):
        for y in range(m):
            # 현재 높이보다 블록 층수가 높을 경우
            # 제거해야할 높이만큼 remove에 저장
            if arr[x][y] >= i:
                remove += arr[x][y] - i
            # 현재 높이보다 블록 층수가 낮을 경우
            # 놓아야할 높이만큼 put에 저장
            else:
                put += i - arr[x][y]
    # print(remove, put)
    # 제거된 블록과 인벤토리에 있던 블록의 수가 놓아야할 블록수 보다 같거다 많을 경우
    if remove + b >= put:
        # 현재 res값에 저장된 시간보다 같거나 적게 걸릴경우 res와 idx값 저장
        if put + (remove * 2) <= res:
            res = put + (remove * 2)
            idx = i

print(res, idx)