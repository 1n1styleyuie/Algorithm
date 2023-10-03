import sys

N = int(sys.stdin.readline())
card_dict = {}

for i in range(N):
    card = int(sys.stdin.readline())
    if card in card_dict:
        card_dict[card] += 1
    else:
        card_dict[card] = 1

result = sorted(card_dict.items(), key = lambda x : (-x[1], x[0]))
print(result[0][0])