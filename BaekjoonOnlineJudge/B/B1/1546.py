M = int(input())
num_list = list(map(int, input().split()))

new_list = []

for i in num_list:
    new_list.append(i / max(num_list) * 100)

result = sum(new_list) / M
print(result)