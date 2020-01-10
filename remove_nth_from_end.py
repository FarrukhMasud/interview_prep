# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode(-1)
        x = head
        dummy.next = head
        parent = dummy
        while x is not None:
            if n <= 0:
                parent = parent.next
            x = x.next
            n = n - 1
        parent.next = parent.next.next
        return dummy.next


def add(head: ListNode, x: int) -> ListNode:
    head.next = ListNode(x)
    return head.next


head = ListNode(1)
x = head
print(1)
for i in range(3):
    x.next = ListNode(i + 2)
    print(x.next.val)
    x = x.next

print("===========================================")
sol = Solution()
x = sol.removeNthFromEnd(head, 2)


while x is not None:
    print(x.val)
    x = x.next
