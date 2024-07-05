# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        min_dis = float("inf")
        previous = head
        present = previous.next
        nextt = present.next

        next_idx = 2
        pre_idx = 0
        first_idx = 0

        while nextt != None:
            if (present.val < previous.val and present.val < nextt.val) or (present.val > previous.val and present.val > nextt.val):
                if not pre_idx:
                    first_idx = next_idx
                else:
                    if next_idx - pre_idx < min_dis:
                        min_dis = next_idx - pre_idx
                pre_idx = next_idx
            previous = present
            present = previous.next
            nextt = present.next
            next_idx += 1

        if min_dis == float("inf"):
            return [-1, -1]
        else:
            return [min_dis, pre_idx-first_idx]

