cnt = 0
num_list = []
min_number = 1e9
for i in range(7):
    number = int(input())

    if number % 2 == 1:
        cnt += number
        if number < min_number:
            min_number = number

if cnt == 0:
    print('-1')
else:
    print(cnt)
    print(min_number)