class ListNode:
    def __init__(self, x, next=None):
        self.val = x
        self.next = next


class Solution:
    def _addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        result = ListNode(-1)
        root = result
        carry = 0
        while l1 is not None or l2 is not None:
            x1 = 0 if l1 is None else l1.val
            x2 = 0 if l2 is None else l2.val
            sum = int(x1 + x2 + carry)
            carry = int(sum / 10)
            sum = sum % 10
            result.next = ListNode(int(sum))
            result = result.next
            l1 = l1.next if l1 is not None else None
            l2 = l2.next if l2 is not None else None

        if carry > 0:
            result.next = ListNode(carry)

        return root.next

    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        def reverse(l1: ListNode):
            currentPar = None
            current = l1
            while current:
                temp = current.next
                current.next = currentPar
                # currentPar.next = None
                currentPar = current
                current = temp
            return currentPar

        lx = reverse(l1)
        ly = reverse(l2)
        rx = self._addTwoNumbers(lx, ly)
        return reverse(rx)


head1 = ListNode(7, ListNode(2, ListNode(4, ListNode(3))))
head2 = ListNode(5, ListNode(6, ListNode(4)))
result = Solution().addTwoNumbers(head1, head2)

while result:
    print(result.val)
    result = result.next
