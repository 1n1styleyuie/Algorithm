T = int(input())
for tc in range(1, T+1):
    str1 = str(input())
    s1 = list(str1)
    s1.reverse()
    s2 = ''.join(s1)

    if str1 == s2:
        print(f'#{tc} 1')
    else:
        print(f'#{tc} 0')