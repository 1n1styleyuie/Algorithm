T = int(input())
for tc in range(1, T+1):
    N, N_hex = input().split()
    num = int(N_hex, base=16)
    binary_num = bin(num)[2:]
    while len(binary_num) % 4:
        binary_num = '0' + binary_num
    print(f'#{tc} {binary_num}')