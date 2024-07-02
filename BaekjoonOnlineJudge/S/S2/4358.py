import sys
input = sys.stdin.readline

tree_percent = dict()
cnt = 0
while True:
    tree = input().rstrip()
    if not tree:
        break

    if tree in tree_percent:
        tree_percent[tree] += 1
    else:
        tree_percent[tree] = 1

    cnt += 1


sorted_tree = sorted(tree_percent.items())
for tre in sorted_tree:
    per = (int(tre[1]) / cnt) * 100
    print('%s %0.4f' %(tre[0], per))