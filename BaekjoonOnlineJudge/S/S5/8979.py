n, k = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

# 금, 은, 동 순서로 정렬
arr.sort(key= lambda x : (x[1], x[2], x[3]), reverse=True)

# 국가 번호 찾기
for i in range(n):
    if arr[i][0] == k:
        idx = i

# 같은 메달 수를 가진 경우를 찾으면
# 해당 i 에서 +1 하여 출력
for i in range(n):
    if arr[idx][1:] == arr[i][1:]:
        print(i+1)
        break