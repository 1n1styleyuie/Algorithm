num_list = list(map(int, input().split()))
cnt = 0
for i in num_list:
    cnt += (i ** 2)

print(cnt % 10)