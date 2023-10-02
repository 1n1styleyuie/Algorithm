# 재귀 호출
def binarySearch(low, high, target, arr):
    global cnt
    left = 0
    right = 0
    while low <= high:
        mid = (low + high) // 2
        # 종료조건 : 두번 연속으로 같은 방향으로 찾으면 안된다.
        if left == 2 or right == 2:
            break
        # 1. 가운데 값이 정답인 경우
        if arr[mid] == target:
            cnt += 1
            return mid
        # 2. 정답보다 작은 경우
        elif arr[mid] < target:
            low = mid + 1
            left = 0
            right += 1
        # 3. 정답보다 큰 경우
        else:
            high = mid -1
            left += 1
            right = 0


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    A.sort()
    cnt = 0
    for i in range(M):
        binarySearch(0, N-1, B[i], A)
    print(f'#{tc} {cnt}')