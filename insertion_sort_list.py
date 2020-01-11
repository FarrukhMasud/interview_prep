from typing import List


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def insertNode(self, head: ListNode, x: ListNode) -> ListNode:
        dummy = ListNode(-1)
        dummy.next = head
        parent = dummy
        curr = head
        while curr is not None and curr.val < x.val:
            parent = curr
            curr = curr.next
        t = parent.next
        parent.next = x
        if parent.next != t:
            parent.next.next = t
        return dummy.next

    def insertionSortList(self, head: ListNode) -> ListNode:
        if head is None:
            return head
        head1 = head
        curr = head.next
        head1.next = None
        while curr is not None:
            t = curr.next
            curr.next = None
            head1 = self.insertNode(head1, curr)
            curr = t

        return head1


def createList(vals: List[int]):
    dummy = ListNode(-1)
    x = dummy
    for i in vals:
        x.next = ListNode(i)
        x = x.next
    return dummy.next


def printList(head: ListNode):
    x = head
    while x is not None:
        print(x.val)
        x = x.next


def createSortedList(x: List[int]) -> ListNode:
    head = ListNode(x[0])
    sol = Solution()
    for i in range(1, len(x)):
        y = ListNode(x[i])
        head = sol.insertNode(head, y)
    return head
