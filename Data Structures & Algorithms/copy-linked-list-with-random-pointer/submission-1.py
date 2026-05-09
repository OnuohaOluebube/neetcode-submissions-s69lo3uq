"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':

        oldToNew = {}

        curr = head

        while curr:
            copy = Node(curr.val)
            oldToNew[curr] = copy

            curr = curr.next

        curr = head
        while curr:
            copy = oldToNew[curr]
            copy.next = oldToNew.get(curr.next, None)
            copy.random = oldToNew.get(curr.random, None)
            curr = curr.next

        return oldToNew.get(head, None)

        