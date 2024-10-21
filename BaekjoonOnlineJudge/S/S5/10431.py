# 10431 s5
import sys
input = sys.stdin.readline

p = int(input())
for _ in range(p):
    arr = list(map(int, input().split()))
    cnt = 0
    # 반 아이들은 20명
    for i in range(1, 21):
        for j in range(i+1, 21):
            # 뒤에 있는 친구가 앞에 있는 친구보다 키가 작을 경우 바꿔주고 카운트
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
                cnt += 1
    
    print(arr[0], cnt)
