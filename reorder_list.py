class ListNode:
    def __init__(self, x, next=None):
        self.val = x
        self.next = next


def printList(x):
    while x:
        print(x.val)
        x = x.next


class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head or not head.next:
            return
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        rev = slow.next
        slow.next = None
        revPar = None
        while rev:
            temp = rev.next
            rev.next = revPar
            revPar = rev
            rev = temp

        current = head
        while current and revPar:
            temp = current.next
            temp1 = revPar.next
            current.next = revPar
            current.next.next = temp
            current = temp
            revPar = temp1


lst = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, ListNode(6))))))
Solution().reorderList(lst)

printList(lst)
