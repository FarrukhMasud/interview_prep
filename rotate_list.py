class ListNode:
    def __init__(self, x, next=None):
        self.val = x
        self.next = next


class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head or not head.next:
            return head
        length = self.length(head)
        if int(k % length) == 0:
            return head
        k = length - int(k % length)

        dummy = ListNode(-1)
        dummy.next = head
        parent = dummy
        current = head
        while current:
            if 0 == k:
                dummy.next = current
                parent.next = None

            parent = current
            current = current.next
            k = k - 1
        parent.next = head
        return dummy.next

    def length(self, root):
        length = 0
        while root:
            length = length + 1
            root = root.next
        return length


# root = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
root = ListNode(0, ListNode(1, ListNode(2)))
print(Solution().length(root))
result = Solution().rotateRight(root, 4)
print(result)

