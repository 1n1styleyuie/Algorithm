import sys
input = sys.stdin.readline

# a : 치킨, b : 피자, c : 햄버거
# x : 치킨, y : 피자, z : 햄버거

a, b, c = map(int, input().split())
x, y, z = map(int, input().split())

ans = 0

'''
반복문에서 첫번째 경우 각각의 식권으로 먹을 수 있는 최대 수를 저장하게 된다.
두번째 반복에서 남은 식권을 교환하여 피자는 치킨3장, 햄버거는 피자3장, 치킨은 햄버거3장으로 먹을 수 있는 최대 수를 저장한다.
세번째 반복에서도 마찬가지로 남은 식권을 교환하여 피자는 치킨3장, 햄버거는 피자3장, 치킨은 햄버거3장으로 먹을 수 있는 최대 수를 저장한다.
식권을 4번 교환하지 않는 이유는 치킨 식권으로 교환하려는 햄버거 식권은 치킨 식권을 (치킨 -> 피자 -> 햄버거) 교환을 하고 난 남은 햄버거 식권이다.
따라서 치킨을 먹을 수 있는 최대 수를 이미 첫번째 경우에서 구했기 때문에 더이상 계산할 필요가 없다.
'''

for _ in range(3):
    # 치킨 교환
    chicken = min(a, x)
    ans += chicken
    a -= chicken
    x -= chicken
    # 피자 교환
    pizza = min(b, y)
    ans += pizza
    b -= pizza
    y -= pizza
    # 햄버거 교환
    hamburger = min(c, z)
    ans += hamburger
    c -= hamburger
    z -= hamburger
    # 치킨 = 햄버거 // 3, 피자 = 치킨 // 3, 햄버거 = 피자 // 3
    x, y, z = z // 3, x // 3, y // 3


print(ans)