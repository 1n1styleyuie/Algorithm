a, b = map(str, input().split())
a = int(a, 2)
b = int(b, 2)
res = a + b
print(bin(res)[2:])