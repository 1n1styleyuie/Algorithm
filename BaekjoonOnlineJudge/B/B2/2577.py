A = int(input())
B = int(input())
C = int(input())

num_lst = list(str(A * B * C))

answer = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

for num in num_lst:
    answer[int(num)] += 1

for ans in answer:
    print(ans)
