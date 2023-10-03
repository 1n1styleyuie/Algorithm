import sys

N = int(sys.stdin.readline())
cards = {
    'STRAWBERRY' : 0,
    'BANANA' : 0,
    'LIME' : 0,
    'PLUM' : 0
}

for i in range(N):
    fruit, x = sys.stdin.readline().split()
    cards[fruit] += int(x)


if 5 in cards.values():
    print('YES')
else:
    print('NO')

# import sys

# T = sys.stdin.readline()
# banana_count = 0
# strawberry_count = 0
# lime_count = 0
# plum_count = 0

# for i in range(T):
#     card, card_num = sys.stdin.readline().split()
#     card_num = int(card_num)
#     if card == 'BANANA':
#         banana_count += card_num
#     elif card == 'STRAWBERRY':
#         strawberry_count += card_num
#     elif card == 'LIME':
#         lime_count += card_num
#     elif card == 'PLUM':
#         plum_count += card_num

# if banana_count == 5 or strawberry_count == 5 or lime_count == 5 or plum_count == 5:
#     print('YES')
# else:
#     print('NO')