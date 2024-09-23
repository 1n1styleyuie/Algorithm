# 30458 s4
import sys
input = sys.stdin.readline

n = int(input())
s = input().rstrip()

cnt = {}

# 문자열을 딕셔너리에 카운트하여 저장
for i in range(n):
    if s[i] in cnt:
        cnt[s[i]] += 1
    else:
        cnt[s[i]] = 1

# 가운데 글자는 빼줌
if n % 2 == 1:
    cnt[s[n//2]] -= 1

flg = True

# 짝수개일때만 팰린드롬이 가능
for c in cnt:
    if cnt[c] % 2 == 1:
        flg = False
        break

if flg:
    print('Yes')
else:
    print('No')