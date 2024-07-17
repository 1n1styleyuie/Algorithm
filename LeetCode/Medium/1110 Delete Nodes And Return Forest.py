# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        lst = []

        # root는 to_delete되고 난 후 트리의 루트 노드에서 시작한 트리이다.
        # 따라서 해당 트리를 lst에 더해줘야 한다.
        root = self._find(root, to_delete, lst)

        # 결과값을 lst에 저장하여 return
        # 없을경우 빈 리스트가 return
        if root:
            lst.append(root)

        return lst

        
    def _find(self, node: Optional[TreeNode], to_delete: List[int], lst: List[int]) -> List[TreeNode]:
        # 값이 없으면 None
        if not node:
            return None

        # 자식 노드로 재귀를 돌려 값이 있는지를 확인
        node.left = self._find(node.left, to_delete, lst)
        node.right = self._find(node.right, to_delete, lst)

        # 현재 노드 값이 삭제할 노드값이라면
        # 왼쪽이나 오른쪽 자식 노드에 트리 구조가 있다면 그 트리노드를 lst에 저장
        # 이후 현재 노드의 값을 None으로 바꾸어 접근하지 못하도록 함
        if node.val in to_delete:

            if node.left:
                lst.append(node.left)
            if node.right:
                lst.append(node.right)
            return None
        # 노드가 삭제되는 것이 없다면 node를 그대로 반환
        return node