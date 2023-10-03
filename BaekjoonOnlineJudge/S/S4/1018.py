import sys
input = sys.stdin.readline


n, m = map(int, input().split())
arr = [list(input()) for _ in range(n)]
cnt = []

for i in range(n-7):
    for j in range(m-7):
        w = 0
        b = 0
        for k in range(i, i+8):
            for h in range(j, j+8):
                if (k+h)%2 == 0: # 짝
                    if arr[k][h] != 'W': # b
                        w += 1 # w
                    else: # w
                        b += 1 # b
                else: # 홀
                    if arr[k][h] != 'W': # b
                        b += 1 # b
                    else: # w
                        w += 1 # w
        cnt.append(w)
        cnt.append(b)
print(min(cnt))
