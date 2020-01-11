from queue import PriorityQueue
from typing import List
from insertion_sort_list import createList
from insertion_sort_list import ListNode
from insertion_sort_list import printList


class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        dummyNode = ListNode(-1)
        x = dummyNode
        while True:
            minValue = None
            minIndex = -1
            for index, l in enumerate(lists):
                if l is None:
                    continue
                if minValue is None or l.val < minValue:
                    minIndex = index
                    minValue = l.val
            if minIndex < 0:
                break
            tmp = lists[minIndex].next
            x.next = lists[minIndex]
            x = x.next
            x.next = None
            lists[minIndex] = tmp

        return dummyNode.next


lst = [createList([1, 4, 5]), createList([3, 4]), createList([2, 8]), None]
# lst = []

sol = Solution()
result = sol.mergeKLists(lst)

printList(result)
