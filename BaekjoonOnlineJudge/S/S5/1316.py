import sys
input = sys.stdin.readline

n = int(input())
arr = []
for _ in range(n):
    arr.append(input())

res = n
for s in arr:
    for i in range(len(s)-1):
        # 뒷문자랑 같으면 pass
        if s[i] == s[i+1]:
            pass
        # 그 외 경우 문장에서 해당 문자 이후에 같은 문자가 나올경우
        # res - 1하고 break
        elif s[i] in s[i+1:]:
            res -= 1
            break

print(res)