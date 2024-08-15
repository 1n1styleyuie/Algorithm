import sys
input = sys.stdin.readline

n = int(input())
fruits = list(map(int, input().split()))


left = 0
fruits_cnt = {}
max_cnt = 0

# 오른쪽 포인터를 이동시켜가면서 확인
for right in range(n):
    # 과일 수 카운트
    if fruits[right] in fruits_cnt:
        fruits_cnt[fruits[right]] += 1
    else:
        fruits_cnt[fruits[right]] = 1

    # 과일 수가 2개가 넘을 경우
    while len(fruits_cnt) > 2:
        # fruits[left], 즉 앞쪽 과일을 뺀다
        fruits_cnt[fruits[left]] -= 1
        # 빼고 난 후 해당 과일이 fruits_cnt에 없을 경우 딕셔너리에서 삭제
        if fruits_cnt[fruits[left]] == 0:
            del fruits_cnt[fruits[left]]
        # 앞 포인터의 위치를 이동
        left += 1
    
    # 두개만 남은 경우에 가장 긴 경우를 저장
    max_cnt = max(max_cnt, right - left + 1)

print(max_cnt)