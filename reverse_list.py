class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        currentPar = None
        current = head
        while current:
            temp = current.next
            current.next = currentPar
            # currentPar.next = None
            currentPar = current
            current = temp
        return currentPar

