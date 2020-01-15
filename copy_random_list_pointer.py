class Solution:
    def copyRandomList(self, head: "Node") -> "Node":
        if head is None:
            return head
        x = head
        cache = dict()

        while x is not None:
            cache[x] = Node(x.val)
            x = x.next

        x = head
        while x is not None:
            y = cache[x]
            if x.next in cache:
                y.next = cache[x.next]
            if x.random in cache:
                y.random = cache[x.random]
            x = x.next
        return cache[head]
