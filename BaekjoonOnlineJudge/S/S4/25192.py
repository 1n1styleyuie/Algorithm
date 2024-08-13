import sys
input = sys.stdin.readline

n = int(input())
cnt = 0
s = {}
for _ in range(n):
    a = input().rstrip()
    # ENTER인 경우 딕셔너리 초기화
    if a == 'ENTER':
        s = {}
    else:
        # 이미 사람이 딕셔너리에 있을 경우
        if a in s:
            s[a] += 1
        # 없으면 cnt +1
        else:
            s[a] = 1
            cnt += 1

print(cnt)