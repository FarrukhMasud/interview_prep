import java.util.*;

class ListNode {
    int val;
    ListNode next;

    ListNode(int x) {
        val = x;
    }
}

class Solution {
    public ListNode mergeKLists(ListNode[] lists) {
        Queue<ListNode> queue = new PriorityQueue<>(new Comparator<ListNode>() {
            @Override
            public int compare(ListNode l1, ListNode l2) {
                if (l1.val < l2.val) {
                    return -1;
                } else if (l1.val > l2.val) {
                    return 1;
                }

                return 0;
            }
        });
        ListNode dummy = new ListNode(-1);
        ListNode x = dummy;

        for (ListNode node : lists) {
            if (node != null) {
                queue.offer(node);
            }
        }

        while (!queue.isEmpty()) {
            ListNode node = queue.poll();
            ListNode next = node.next;
            node.next = null;
            x.next = node;
            x = x.next;
            if (next != null) {
                queue.offer(next);
            }
        }

        return dummy.next;
    }
}