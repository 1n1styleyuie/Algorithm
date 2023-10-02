T = int(input())
for tc in range(1, T+1):
    test_case, N = input().split()
    str_list = list(map(str, input().split()))
    count_zro = 0
    count_one = 0
    count_two = 0
    count_thr = 0
    count_for = 0
    count_fiv = 0
    count_six = 0
    count_svn = 0
    count_egt = 0
    count_nin = 0
    for i in range(len(str_list)):
        if str_list[i] == 'ONE':
            count_one += 1
        elif str_list[i] == 'TWO':
            count_two += 1
        elif str_list[i] == 'THR':
            count_thr += 1
        elif str_list[i] == 'FOR':
            count_for += 1
        elif str_list[i] == 'FIV':
            count_fiv += 1
        elif str_list[i] == 'SIX':
            count_six += 1
        elif str_list[i] == 'SVN':
            count_svn += 1
        elif str_list[i] == 'EGT':
            count_egt += 1
        elif str_list[i] == 'NIN':
            count_nin += 1
        else:
            count_zro += 1
    print(test_case)
    print('ZRO '*count_zro, 'ONE '*count_one, 'TWO '*count_two,
          'THR '*count_thr, 'FOR '*count_for, 'FIV '*count_fiv,
          'SIX '*count_six, 'SVN '*count_svn, 'EGT '*count_egt,
          'NIN '*count_nin)