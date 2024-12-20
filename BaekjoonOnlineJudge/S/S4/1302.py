# 1302 s4
import sys
input = sys.stdin.readline


n = int(input())
book = {}

for _ in range(n):
    name = input().rstrip()
    if name in book:
        book[name] += 1
    else:
        book[name] = 1

# 책 개수를 모두 받고 난 다음 lambda를 활용하여 정렬
# -x[1]을 통해 책 개수를 내림차순으로, x[0]을 통해 알파벳 오름차순으로 정렬
res = sorted(book.items(), key = lambda x : (-x[1], x[0]))

print(res[0][0])