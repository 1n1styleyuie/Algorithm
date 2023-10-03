T = int(input())
for tc in range(T):
    num_list = list(map(int, input().split()))
    cnt = 0
    even_list = []
    for i in num_list:
        if i % 2 == 0:
            even_list.append(i)
            cnt += i
    print(cnt, min(even_list))