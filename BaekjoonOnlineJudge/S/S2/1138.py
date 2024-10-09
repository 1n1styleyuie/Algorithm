# 1138 s2
import sys
input = sys.stdin.readline


n = int(input())
arr = list(map(int, input().split()))
ans = [0] * n

# i는 사람 번호, j는 위치 번호
# cnt는 앞에 비어있는 수를 저장
for i in range(n):
    cnt = 0
    for j in range(n):
        # 키 순으로 1부터 시작했기 때문에 cnt값과 arr에 저장된 값이 같고
        # 현 위치가 비어있는 자리라면 그 자리에 사람 번호 저장하고 break
        if cnt == arr[i] and ans[j] == 0:
            ans[j] = i + 1
            break
        # 그냥 비어있고 아직 cnt가 arr과 같지 않다면 cnt + 1
        if ans[j] == 0:
            cnt += 1

print(*ans)