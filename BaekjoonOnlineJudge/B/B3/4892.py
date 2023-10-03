count = 1
while True:
    n0 = int(input())
    if n0 == 0:
        break
    n1 = 3 * n0
    if n1 % 2 == 1:
        n2 = (n1 + 1) / 2
        n3 = 3 * n2
        n4 = n3 // 9
        print(f"{count}. odd {int(n4)}")
    else:
        n2 = n1 / 2
        n3 = 3 * n2
        n4 = n3 // 9
        print(f"{count}. even {int(n4)}")
    count += 1