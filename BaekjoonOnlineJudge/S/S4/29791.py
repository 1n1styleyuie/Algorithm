n, m = map(int, input().split())

A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort()
B.sort()

a = 0
b = 0
pa = 0
pb = 0

for i in A:
    if pa == 0 or i - pa >= 100:
        a += 1
        pa = i
            
for i in B:
    if pb == 0 or i - pb >= 360:
        pb = i
        b += 1

print(a, b)