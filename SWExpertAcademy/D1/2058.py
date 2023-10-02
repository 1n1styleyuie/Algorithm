def sumofdigit(num):
    result = sum(int(i) for i in num)
    return result

num = input()
print(sumofdigit(num))