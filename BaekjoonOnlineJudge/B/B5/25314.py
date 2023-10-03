N = int(input())

result = 'int'
for i in range(N//4):
    result = 'long ' + result

print(result)