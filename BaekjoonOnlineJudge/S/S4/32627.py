# 32627 s4
import sys
input = sys.stdin.readline

'''
a~z까지 개수를 구한 뒤 몇개를 스킵해야 하는지 기록한다.
m의 개수보다 크거나 같으면 해당 문자 전체를 스킵하고, 
m의 개수보다 작다면 남은 문자만큼 무시한다.
'''
n, m = map(int, input().split())
ss = input().rstrip()

cnt = [0] * 26
s_cnt = [0] * 26

for s in ss:
    cnt[ord(s) - ord('a')] += 1

for i in range(26):
    if cnt[i] > m:
        s_cnt[i] = m
        break
    else:
        s_cnt[i] = cnt[i]
        m -= cnt[i]

res = ''
for s in ss:
    if s_cnt[ord(s) - ord('a')] > 0:
        s_cnt[ord(s) - ord('a')] -= 1
        continue
    res += s

print(res)