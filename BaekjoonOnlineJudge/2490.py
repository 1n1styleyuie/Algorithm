for i in range(3):
    num_list = list(map(int, input().split()))
    cnt = 0
    for j in num_list:
        cnt += j

    if cnt == 4:
        print('E')
    elif cnt == 3:
        print('A')
    elif cnt == 2:
        print('B')
    elif cnt == 1:
        print('C')
    elif cnt == 0:
        print('D')