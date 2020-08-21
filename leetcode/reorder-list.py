# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head):
        """
        Do not return anything, modify head in-place instead.
        """
        # original_head = head

        p1 = p2 = head

        while p2.next != None and p2.next.next != None:
            p1 = p1.next
            p2 = p2.next.next

        middle = p1
        current = middle.next
        prev = None
        while current != None:
            after_current = current.next
            current.next = prev
            prev = current

            # connect middle to...
            middle.next = current

            current = after_current

        current = head
        after_middle = middle.next

        while current.next.val != after_middle.val:
            next_current = current.next
            next_after_middle = after_middle.next

            middle.next = next_after_middle

            after_middle.next = current.next
            current.next = after_middle

            current = next_current
            after_middle = next_after_middle
