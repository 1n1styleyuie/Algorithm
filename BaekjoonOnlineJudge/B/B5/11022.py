T = int(input())

count = 1

for i in range(T):
    a, b = map(int, input().split())
    print(f'Case #{count}: {a} + {b} = {a + b}')
    count += 1