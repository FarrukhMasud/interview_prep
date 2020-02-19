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
