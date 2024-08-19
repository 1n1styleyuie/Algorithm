import sys
input = sys.stdin.readline

pikachu = ["pi", "ka", "chu"]
s = input().rstrip()
tmp = ""
flg = True

for i in range(len(s)):
    tmp += s[i]
    if tmp in pikachu:
        tmp = ""
    if len(tmp) >= 3:
        flg = False
        break

# flg가 True이고 tmp에 아무것도 없을 경우에만 YES 리턴
if flg and tmp == "":
    print("YES")
else:
    print("NO")