# 1439 s5
import sys
input = sys.stdin.readline

s = input().rstrip()


# arr1은 1을 제거한 상태, cnt1은 0을 카운트
# arr2는 0을 제거한 상태, cnt2는 1을 카운트
arr1 = s.split('1')
arr2 = s.split('0')

cnt1 = 0
cnt2 = 0

for i in arr1:
    if '0' in i:
        cnt1 += 1
    
for i in arr2:
    if '1' in i:
        cnt2 += 1

print(min(cnt1, cnt2))