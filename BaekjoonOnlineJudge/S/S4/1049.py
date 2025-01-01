# 18405 g5
import sys
input = sys.stdin.readline


n, m = map(int, input().split())
arr1 = []
arr2 = []
for _ in range(m):
    a, b = map(int, input().split())
    arr1.append(a)
    arr2.append(b)


# a1은 패키지로 구매했을 때 가장 저렴한 경우
# a2는 낱개로 구매했을 때 가장 저렴한 경우
a1 = min(arr1)
a2 = min(arr2)

# 패키지가 낱개로 6개 구매하는 것보다 저렴한 경우
if a1 < a2 * 6:
    if a1 < (n % 6) * a2:
        print((n//6) * a1 + a1)
    else:
        print((n//6) * a1 + (n % 6) * a2)
# 낱개로 6개 구매하는 것이 패키지보다 저렴한 경우
elif a1 >= a2 * 6:
    print(n * a2)