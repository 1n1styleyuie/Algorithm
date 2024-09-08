# 1969 s4
import sys
input = sys.stdin.readline


n, m = map(int, input().split())
arr = [list(input().rstrip()) for _ in range(n)]
res = ''
distance = 0

# 글자 수 카운트한 결과로 res에 문자열을 저장하고 distance에 거리를 더한다.
for j in range(m):
    a, t, g, c = 0, 0, 0, 0
    for i in range(n):
        if arr[i][j] == 'A':
            a += 1
        elif arr[i][j] == 'T':
            t += 1
        elif arr[i][j] == 'G':
            g += 1
        elif arr[i][j] == 'C':
            c += 1
    
    # 사전순으로 저장
    if max(a, t, g, c) == a:
        res += 'A'
        distance += t + g + c
    elif max(a, t, g, c) == c:
        res += 'C'
        distance += a + t + g
    elif max(a, t, g, c) == g:
        res += 'G'
        distance += a + t + c
    elif max(a, t, g, c) == t:
        res += 'T'
        distance += a + g + c

print(res)
print(distance)