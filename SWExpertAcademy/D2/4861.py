T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(input()) for _ in range(N)]
    result = 0
    for i in range(N):
        for j in range(N):
            str1_list = []
            str2_list = []
            for k in range(M):
                if (j+M) <= N:
                    str1_list.append(arr[i][j+k])
            str2_list = str1_list[::-1]
            if str2_list == str1_list and str1_list != [] and str2_list != []:
                result = str1_list

    for j in range(N):
        for i in range(N):
            str3_list = []
            str4_list = []
            for k in range(M):
                if (i+M) <= N:
                    str3_list.append(arr[i+k][j])
            str4_list = str3_list[::-1]
            if str4_list == str3_list and str3_list != [] and str4_list != []:
                result = str3_list
    res = ''.join(result)
    print(f'#{tc} {res}')