class Solution:
    def reverseList(self, head):
        if not head or not head.next:
            return head
        ans = ListNode(head.val)
        head = head.next
        while head:
            temp = ListNode(head.val)
            temp.next = ans
            ans = temp
            head = head.next
        return temp
