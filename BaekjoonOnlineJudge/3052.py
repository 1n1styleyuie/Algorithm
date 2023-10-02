num_list = []

for i in range(10):
    num = int(input())
    num_list.append(num % 42)

print(len(set(num_list)))