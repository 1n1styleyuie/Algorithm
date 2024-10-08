# 16198 s1
import sys
input = sys.stdin.readline


def f(total):
    global ans
    # 리스트에 두개만 있다면 더이상 모을 수 없기 떄문에 최대값을 저장 후 return
    if len(w) == 2:
        ans = max(ans, total)
        return
    
    # tmp에 현재 값을 저장해두고 현 위치 pop한 뒤 재귀
    # 그리고 백트래킹을 위해 insert하고 total값에서 다시 원상태로 돌려줌
    for i in range(1, len(w)-1):
        total += w[i-1] * w[i+1]
        tmp = w[i]
        w.pop(i)
        f(total)
        w.insert(i, tmp)
        total -= w[i-1] * w[i+1]


n = int(input())
w = list(map(int, input().split()))

ans = 0

f(0)
print(ans)