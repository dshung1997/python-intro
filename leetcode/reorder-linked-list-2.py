# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        # original: 1 => [2 => 3 => 4] => 5 => 6
        # reversed: 1 => [4 => 3 => 2] => 5 => 6
        # m = 2, n = 4
        # pivot = 1
        # last = 2 - the last node of the reversed part

        # if m == 1, pivot == None
        # (if pivot...) statement is for when m == 1

        pivot = None
        current = head
        for _ in range(m - 1):
            pivot = current
            current = current.next

        prev = None  # the previous node in the original linked list
        count = 0
        last = current

        while current != None and count <= (n - m):
            after_current = current.next
            current.next = prev
            prev = current

            current = after_current
            count += 1

        # connect the reversed part to the remaining part
        last.next = current

        # connect pivot to the reversed part
        if pivot:
            pivot.next = prev
            return head
        else:
            return prev
