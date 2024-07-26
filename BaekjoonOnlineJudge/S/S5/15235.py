import sys
input = sys.stdin.readline
from collections import deque

n = int(input())
arr = list(map(int, input().split()))

q = deque()
idx = 1
# 인덱스 포함해서 저장
for i in range(len(arr)):
    q.append([arr[i], idx])
    idx += 1


cnt = 0
res = []
while q:
    student, st_idx = q.popleft()
    cnt += 1
    student -= 1
    # 0이 되면 res에 저장
    if student == 0:
        res.append([cnt, st_idx])
    # 아니라면 다시 q에 저장
    else:
        q.append([student, st_idx])

# 인덱스 순으로 정렬 후 출력
res.sort(key= lambda x: x[1])
for i in res:
    print(i[0], end=" ")