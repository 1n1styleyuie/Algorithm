# 1991 s1
import sys
input = sys.stdin.readline

# 전위순회는 root, left, right 순
def preorder(root):
    if root != '.':
        print(root, end='')
        preorder(tree[root][0])
        preorder(tree[root][1])


# 중위순회는 left, root, right 순
def inorder(root):
    if root != '.':
        inorder(tree[root][0])
        print(root, end='')
        inorder(tree[root][1])


# 후위순회는 left, right, root 순
def postorder(root):
    if root != '.':
        postorder(tree[root][0])
        postorder(tree[root][1])
        print(root, end='')


n = int(input())
tree = {}
for _ in range(n):
    root, left, right = input().rstrip().split()
    tree[root] = [left, right]

# 노드의 이름은 A부터 매겨지기 떄문에 항상 A가 root노드
preorder('A')
print()
inorder('A')
print()
postorder('A')