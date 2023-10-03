n, l = map(int, input().split())
count = 0
now = 0
for _ in range(n):
    d, r, g = map(int, input().split())
    count += (d-now)
    now = d
    if count % (r+g) <= r:
        count += (r-(count%(r+g)))
count += (l-now)
print(count)