# 20310 s3
import sys
input = sys.stdin.readline

s = list(input().rstrip())

zero = s.count('0')
one = s.count('1')

# 사전순으로 빠르게 하기 위해 앞에서 부터 1을 제거
# 단 1을 제거할 때 절반 이상 제거하지 않도록 한다
tmp = 0
for i in s:
    if tmp == one // 2:
        break
    
    if i == '1':
        s.remove(i)
        tmp += 1

# 문자열을 역순으로 하여 뒤에서부터 0을 제거
# 절반 이상 제거하지 않도록 한다
tmp = 0
s = s[::-1]
for i in s:
    if tmp == zero // 2:
        break

    if i == '0':
        s.remove(i)
        tmp += 1

# 역순으로 돌렸었기 때문에 다시 역순으로 돌려 출력
s = s[::-1]
print(''.join(s))