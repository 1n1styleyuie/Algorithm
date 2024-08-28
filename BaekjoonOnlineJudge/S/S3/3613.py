# 3613 s3
import sys
input = sys.stdin.readline

s = input().rstrip()
ans = ''
if s[0].islower():
    # C++ -> Java
    if '_' in s:
        # '_' 연속 두개라면 에러
        if '__' in s:
            print('Error!')
            exit()
        # 맨 앞 혹은 맨 뒤 문자가 '_' 이라면 에러
        if s[0] == '_' or s[-1] == '_':
            print('Error!')
            exit()
        flg = False
        for i in range(len(s)):
            # '_'라면 flg를 True로 바꿈
            if s[i] == '_':
                flg = True
            # 대문자라면 에러
            elif s[i].isupper():
                ans = 'Error!'
                break
            else:
                # flg가 True일 경우 대문자로 바꿔서 ans에 더해주고 flg를 False로 초기화
                if flg:
                    ans += s[i].upper()
                    flg = False
                else:
                    ans += s[i]
    # Java -> C++
    else:
        for i in range(len(s)):
            # 대문자일 경우 '_'를 붙이고 소문자로 바꿔서 ans에 저장
            if s[i].isupper():
                ans += '_' + s[i].lower()
            else:
                ans += s[i]
else:
    ans = 'Error!'

print(ans)