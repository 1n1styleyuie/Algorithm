# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        parent_set = set()  # 부모 노드를 저장하는 집합
        child_set = set()   # 자식 노드를 저장하는 집합

        nodes = {}  # 각 노드의 자식 정보를 저장하는 딕셔너리
        for description in descriptions:
            parent = description[0]
            child = description[1]
            is_left = description[2]

            parent_set.add(parent)  # 부모 노드 추가
            child_set.add(child)    # 자식 노드 추가

            if parent not in nodes:
                nodes[parent] = [None, None]  # 왼쪽, 오른쪽 자식 노드를 저장할 리스트 초기화
            if child not in nodes:
                nodes[child] = [None, None]   # 자식 노드도 초기화 (나중에 부모가 될 수 있음)

            if is_left:
                nodes[parent][0] = child  # 왼쪽 자식 노드로 설정
            else:
                nodes[parent][1] = child  # 오른쪽 자식 노드로 설정

        # 루트 노드는 부모 집합에 있지만 자식 집합에는 없는 노드
        root_val = (parent_set - child_set).pop()
        ans = TreeNode(root_val)  # 루트 노드 생성

        # BFS를 위해 큐를 사용
        q = deque()
        q.append((root_val, ans))

        while q:
            parent, node = q.popleft()

            left = nodes[parent][0]
            right = nodes[parent][1]

            if left is not None:
                node.left = TreeNode(left)  # 왼쪽 자식 노드 생성
                q.append((left, node.left))  # 큐에 추가
            
            if right is not None:
                node.right = TreeNode(right)  # 오른쪽 자식 노드 생성
                q.append((right, node.right))  # 큐에 추가

        return ans  # 생성된 이진 트리의 루트 노드 반환