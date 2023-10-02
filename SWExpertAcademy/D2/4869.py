T = int(input())
for tc in range(1, T+1):
    n = (int(input())//10)
    tile = [0, 1, 3]
    for i in range(3, n+1):
        tile.append(tile[i-1]+ 2 * tile[i-2])
    print(f'#{tc} {tile[n]}')