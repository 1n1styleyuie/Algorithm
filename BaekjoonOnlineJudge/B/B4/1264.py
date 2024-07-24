while True:
    ss = input()
    if ss == '#':
        break
    cnt = 0
    for s in ss:
        # if s.islower():
        if s in ['a', 'i', 'e', 'o', 'u', 'A', 'I', 'E', 'O', 'U']:
            cnt += 1

    print(cnt)