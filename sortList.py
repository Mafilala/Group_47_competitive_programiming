class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        def mid_node(node):
            if not node or not node.next:
                return node
            fast, slow = node.next, node
            while fast and fast.next:
                slow = slow.next
                fast = fast.next
                if fast:
                    fast = fast.next
            return slow
        def merge(node1, node2):
            merged = ListNode(0)
            dummy = merged
            while node1 and node2:
                if node1.val <= node2.val:
                    merged.next = ListNode(node1.val)
                    node1 = node1.next
                    merged = merged.next
                else:
                    merged.next = ListNode(node2.val)
                    node2 = node2.next
                    merged = merged.next
            if node1:
                merged.next = node1
            if node2:
                merged.next = node2
            return dummy.next

        def sort(node):
            if not node or not node.next:
                return node
            mid = mid_node(node)
            temp = mid.next
            mid.next = None
            left = sort(node)
            right = sort(temp)
            return merge(left, right)
        return sort(head)
