# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # def node2list(self, node1 : ListNode) -> List:
    #     res_list = []
    #     while node1 != None:
    #         res_list.append(node1.val)
    #         node1 = node1.next
    #     return res_list


    # def list2node(self, list1 : List) -> ListNode:
    #     result_node = ListNode()
    #     for i, num in enumerate(list1):
    #         if i == 0:
    #             result_node.val = num
    #         else:
    #             node = result_node
    #             while node.next != None:
    #                 node = node.next
    #             node.next = ListNode(num)
    #     return result_node


    # def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
    #     cnt = 0
    #     answer = []
    #     head_list = self.node2list(head)
    #     for i in range(1, len(head_list)):
    #         if head_list[i] == 0:
    #             answer.append(cnt)
    #             cnt = 0
    #         else:
    #             cnt += head_list[i]
    #     return self.list2node(answer)


    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        modify = head.next
        next_sum = modify

        
        while next_sum:
            sum = 0
            while next_sum.val != 0:
                sum += next_sum.val
                next_sum = next_sum.next

            modify.val = sum
            next_sum = next_sum.next
            modify.next = next_sum
            modify = modify.next

        return head.next