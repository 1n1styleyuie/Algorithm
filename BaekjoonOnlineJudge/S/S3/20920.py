import sys
input = sys.stdin.readline

n, m = map(int, input().split())
word = {}
for _ in range(n):
    s = input().rstrip()
    if len(s) >= m:
        if s in word:
            word[s] += 1
        else:
            word[s] = 1

# lambda를 사용할때 정렬하려고 하는 조건을 순서대로 적으면 된다.
# 자주 나오는 단어, 길이가 긴 단어, 알파벳 사전순으로 정렬한다.
word = sorted(word.items(), key=lambda x : (-x[1], -len(x[0]), x[0]))

for i in word:
    print(i[0])