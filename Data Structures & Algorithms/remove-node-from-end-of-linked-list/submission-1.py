# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        nodes = []


        curr = head

        while curr:
            nodes.append(curr)
            curr = curr.next

        targetnode = len(nodes) - n

        if targetnode == 0:
            return head.next
        nodes[targetnode - 1].next = nodes[targetnode].next
        print(nodes)
        print(head)
        return head