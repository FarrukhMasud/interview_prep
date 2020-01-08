class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
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


sol = Solution()
number1 = ListNode(9)
number1.next = ListNode(9)
number1.next.next = ListNode(9)


number2 = ListNode(1)
# number2.next = ListNode(6)
# number2.next.next = ListNode(4)

x = sol.addTwoNumbers(number1, number2)
print(x)
