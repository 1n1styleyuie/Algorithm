class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        # 시작 노드로 가는 경로와 목적지 노드로 가는 경로를 저장할 리스트
        s, d = [], []
        
        # 시작 노드로 가는 경로
        self.find(root, startValue, s)
        # 목적지 노드로 가는 경로
        self.find(root, destValue, d)
        
        # 두 경로의 공통 부분을 제거
        while len(s) and len(d) and s[-1] == d[-1]:
            s.pop()
            d.pop()

        # 시작 노드로부터 공통 조상까지 U 이동 후 공통 조상에서 목적지까지의 경로
        return "".join("U" * len(s)) + "".join(reversed(d))
        
    def find(self, n: Optional[TreeNode], val: int, path: List[str]) -> bool:
        # 현재 노드가 찾는 값이면 True 반환
        if n.val == val:
            return True
        
        # 아래 과정에서 결국 다시 재귀함수로 돌아가서 추가된 상태로 반환되기 때문에
        # 왼쪽 자식 노드에서 값을 찾고 경로에 L 추가
        if n.left and self.find(n.left, val, path):
            path += "L"
        # 오른쪽 자식 노드에서 값을 찾고 경로에 R 추가
        elif n.right and self.find(n.right, val, path):
            path += "R"
        # 값을 찾았으면 path 리스트가 비어있지 않으므로 그대로 반환, 찾지 못했으면 빈 리스트 반환
        return path